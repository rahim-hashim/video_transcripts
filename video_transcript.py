import os
import sys
import time
import pickle
import whisper
import pprint
import argparse
from tqdm import tqdm
from datetime import datetime
from collections import defaultdict
from pytubefix import YouTube, Playlist, Channel
# for slugify
import unicodedata
import re
# remapping Youtube Playlist links to specified directory names
from utils.podcast_yt_links import podcast_playlist_names

def slugify(value, allow_unicode=False):
	"""
	Taken from https://github.com/django/django/blob/master/django/utils/text.py
	Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
	dashes to single dashes. Remove characters that aren't alphanumerics,
	underscores, or hyphens. Convert to lowercase. Also strip leading and
	trailing whitespace, dashes, and underscores.
	"""
	value = str(value)
	if allow_unicode:
		value = unicodedata.normalize('NFKC', value)
	else:
		value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
	value = re.sub(r'[^\w\s-]', '', value)
	return value

def make_transcript_folder():
	if '_Transcripts' not in os.listdir():
		os.mkdir('_Transcripts') 

def load_model(model_name='base'):
	'''
	Import the modules you will be using, and load the whisper model -- `base` is ok, but from the documentation:

	There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. 
	Below are the names of the available models and their approximate memory requirements and inference speed relative 
	to the large model; actual speed may vary depending on many factors including the available hardware.

	|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
	| :----: | :--------: | :----------------: | :----------------: | :-----------: | :------------: |
	|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
	|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
	| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
	| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
	| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |
	'''

	print(f'Loading Whisper Model: {model_name}')
	model = whisper.load_model(model_name)
	print('  Model Loaded.')
	return model

class Video:
	def __init__(self):
		self.title = None
		self.author = None
		self.date = None
		self.url = None
		self.video_path = None
		self.views = None
		self.description = None
		self.author_folder = None
		self.keywords = None
		self.length = None
		self.rating = None
		self.transcript_path = None
		self.transcript_exists = False
		self.transcript = None
		self.timestamps = None

	def get_video(self, source='youtube', playlist_url=None, url=None, local_path=None):
		'''
		Download a video from a source and set the video attributes

		Args:
			source (str): The source of the video. Options are 'youtube' or 'local'
			url (str): The URL of the video. Required if source is 'youtube'
			local_path (str): The local path of the video. Required if source is 'local'

		Returns:
			None
		'''

		if source=='youtube':
			if url == None:
				# ask for the url
				url = input('Enter the URL of the video: ')
			youtube_obj = YouTube(url)
			try:
				youtube_obj.check_availability()
				streams = youtube_obj.streams.filter(only_audio=True)
			except Exception as e:
				print(f'  Error: {e}')
				return
			stream = streams.first()
			current_time_str = datetime.now().strftime('%Y%m%d_%H%M%S')
			video_path = f'youtube_{current_time_str}.mp4'
			# Set video attributes
			self.title = stream.title
			self.author = youtube_obj.author
			self.date = f"{youtube_obj.publish_date:%B %d, %Y}"
			self.url = url
			# rename the author to the specified author name
			if playlist_url and playlist_url in podcast_playlist_names.keys():
				print(f'  Renaming {self.author} to: {podcast_playlist_names[playlist_url]}')
				self.author = podcast_playlist_names[playlist_url]
			self.video_path = video_path
			self.length = youtube_obj.length
			self.rating = youtube_obj.rating
			self.keywords = youtube_obj.keywords
			self.description = youtube_obj.description
			self.views = youtube_obj.views
			self.transcript_exists = self.check_transcript()
			if self.transcript_exists:
				print(f'  Skipping video.')
				return
			print(f'Downloading video from: {url}')
			stream.download(filename=video_path)
			print(f'  Video downloaded to {video_path}')
		elif source=='local':
			if local_path == None:
				raise ValueError('Local Path must be provided for local videos')
			self.video_path = local_path
			self.title = local_path
			self.url = None
			self.author = 'Local File'
			self.date = f"{datetime.now():%B %d, %Y}"
			self.length = None
			self.transcript_exists = self.check_transcript()

		print(f'Video Title: {self.title}')
		print(f'  Author: {self.author}')
		print(f'  Date:   {self.date}')
		if self.length:
			print(f'  Length: {round(self.length/60, 2)}m')
		if self.views:
			print(f'  Views:  {self.views}')
		return True

	def check_transcript(self):
		# see if directory exists, if not create it but replace non-directory characters
		author_name_slug = slugify(self.author)
		author_folder = os.path.join('_Transcripts', author_name_slug)
		self.author_folder = author_name_slug
		if not os.path.exists(author_folder):
			print('Creating directory:', author_folder)
			os.mkdir(author_folder)
		short_date = datetime.strptime(self.date, '%B %d, %Y').strftime('%Y%m%d')
		transcript_path = os.path.join(author_folder, f'{short_date}_{author_name_slug}.md')
		self.transcript_path = transcript_path
		# check if file already exists
		if os.path.exists(transcript_path):
			print(f'  File already exists: {transcript_path}')
			return True
		return False

	def transcribe_video(self, video, model):
		'''Transcribe the video using the whisper model'''
		print('Transcribing Video')
		start_time = time.time()
		output = model.transcribe(video.video_path, fp16=False)
		transcription_time = round((time.time() - start_time)/60, 2)
		print(f'  Transcription Time: {transcription_time} min')
		# print('Output Keys:', output.keys())
		# print('  Segment Keys:', output['segments'][0].keys())
		segments = [text['text'] for text in output['segments']]
		video.transcript = segments
		timestamps = [text['start'] for text in output['segments']]
		video.timestamps = timestamps
		# format value 100000 -> 100.000
		num_words = "{:,}".format(len(segments))
		print(f'  Segments Transcribed: {num_words}')

	def write_yaml(self, f):
		f.write('---\n')
		f.write(f'Date Generated: {datetime.now():%B %d, %Y}\n')
		whisper_version = whisper.__version__
		f.write(f'Transcription Model: whisper medium {whisper_version}\n')
		f.write(f'Length: {self.length}s\n')
		f.write(f'Video Keywords: {self.keywords}\n')
		f.write(f'Video Views: {self.views}\n')
		# rating can either be a float or None
		if self.rating == None:
			f.write('Video Rating: None\n')
		else:
			f.write(f'Video Rating: {round(self.rating, 3)}\n')
		if self.description == None:
			f.write('Video Description: None\n')
		else:
			f.write(f'Video Description: {self.description}\n')
		f.write('---\n\n')

	def write_transcript(self):
		'''Write the transcript to a markdown file'''
		print('Writing transcript to file')
		# if file does not exist, write the transcript
		with open(self.transcript_path, 'w', encoding='utf-8') as f:
			# write yaml front matter
			self.write_yaml(f)
			# write the title and author
			f.write(f'# {self.title}\n')
			f.write(f'**{self.author}:** [{self.date}]({self.url})\n')
			if self.transcript == None:
				raise ValueError('Transcript must be generated before writing')
			for s_index, segment in enumerate(self.transcript):
				# get time stamp and link it to that time in the video
				timestamp = self.timestamps[s_index]
				# get link to the youtube video with the timestamp
				timestamp_link = f'{self.url}&t={timestamp}s'
				timestamp_str = time.strftime('%H:%M:%S', time.gmtime(timestamp))
				f.write(f'* {segment} [[{timestamp_str}]({timestamp_link})]\n')
		f.close()

	def delete_video(self):
		'''Delete the video file'''
		os.remove(self.video_path)
		print(f'Video file deleted: {self.video_path}')

def extract_playlist_urls(args, playlists):
	url_dict = defaultdict(list)
	url_playlist_map = defaultdict(str)
	for playlist_url in playlists:
		playlist = Playlist(playlist_url)
		playlist_url_list = list(playlist.video_urls)
		print(f'Transcribing Playlist: {playlist.title}')
		print(f'  Number of Total Videos: {len(playlist_url_list)}')
		if args.refresh and args.max_load == None:
			print(f'     --refresh specified')
			url_dict[playlist_url].append(playlist_url_list)
		elif args.max_load != None:
			print(f'    --max_load specified {args.max_load} videos')
			url_dict[playlist_url].append(playlist_url_list[:args.max_load])
		else:
			url_dict[playlist_url].append(playlist_url_list)
		# map each video url to the playlist url
		for url in playlist_url_list:
			url_playlist_map[url] = playlist_url
	# flatten the list
	for key, url_list in url_dict.items():
		url_dict[key] = [url for sublist in url_list for url in sublist]
	return url_dict, url_playlist_map

if __name__ == '__main__':
	
	# Parse the command line arguments
	parser = argparse.ArgumentParser(description='Video Transcription')
	parser.add_argument('--source', choices=['youtube', 'local'], 
																	default='youtube', 
																	help='The source of the video')
	parser.add_argument('--refresh', help='If specified, retrieve all playlist links from \'youtube_links.py\' and generate \
										 										 transcripts for only the most recent video in each playlist', 
																	 action='store_true')
	parser.add_argument('--url', help='The URL of the video (required if source is youtube and not refreshing playlists)', default=None)
	parser.add_argument('--local_path', help='The local path of the video (required if source is local)')
	parser.add_argument('--max_load', help='If specified, the max number of videos to transcribe from a playlist',
																		default=1000, type=int)
	parser.add_argument('--break_repeat', help='If specified, break transcription loop once a repeat has been detected', action='store_true')
	parser.add_argument('--git', help='If specified, push the changes to git', action='store_true')

	args = parser.parse_args()
	
	# Load the model
	model = load_model('medium')

	# Check if the transcript folder exists
	make_transcript_folder()

	# Local videos
	if args.local_path:
		args.source = 'local'
		video=Video()
		local_path = args.local_path
		video.get_video(source=args.source, local_path=local_path)
		video.transcribe_video(video, model)
		video.write_transcript()
		sys.exit()

	# Youtube videos
	playlists = []
	if args.refresh:
		# get all the playlist links from youtube_links.py
		playlists = list(podcast_playlist_names.keys())
		print(f'Refreshing playlists from \'youtube_links.py\'.')
		print(f'  Number of Playlists: {len(playlists)}')
	elif args.url and 'playlist' in args.url.lower():
		# Youtube Playlist URL Example: 
		#   https://www.youtube.com/playlist?list=PLdMrbgYfVl-s16D_iT2BJCJ90pWtTO1A4
		#   https://www.youtube.com/watch?v=Bg1LQ_jWliU&list=PLVfJCYRuaJIUNqx6puWYmw7Ug_QsTlA5k
		playlists = [args.url]
	
	if playlists:
		url_dict, url_playlist_map = extract_playlist_urls(args, playlists)
	else:
		url_playlist_map = {}
		url_dict = defaultdict(list)
		url_dict[args.url].append(args.url)

	print(f'Number of Channels: {len(url_dict)}')
	transcribed_url_count = 0
	for c_index, channel in enumerate(tqdm(url_dict.keys())):
		print(f'Transcribing Channel: {channel}')
		# Check if url_dict for channel is empty
		if not url_dict[channel]:
			print(f'No videos to transcribe for {channel}')
			continue
		# iterate through the urls
		for u_index, url in enumerate(url_dict[channel]):
			# Create a video object
			video = Video()
			# Get the video
			if url in url_playlist_map.keys():
				playlist_url = url_playlist_map[url]
			else:
				playlist_url = None
			status = video.get_video(
				source=args.source, 
				playlist_url=playlist_url, 
				url=url
			)
			# Transcribe the video
			if not video.transcript_exists and status != None:
				video.transcribe_video(video, model)
				video.write_transcript()
				video.delete_video()
				transcribed_url_count += 1
			elif status == None and args.break_repeat:
				print(f'Other {len(url_dict[channel]) - u_index} videos in the playlist have already been transcribed.')
				break
	print('Transcription Complete')
	print(f'  Number of Videos Transcribed: {transcribed_url_count}')

	# push to git
	if args.git:
		print('Pushing to Git')
		os.system('git add .')
		os.system('git commit -m "Transcription Update"')
		os.system('git push')
		print('Pushed to Git')