import os
import re
import sys
import tqdm
import pickle
import datetime
import pandas as pd
import seaborn as sns
from utils import fuzzy_lookup
import matplotlib.pyplot as plt
from collections import defaultdict

news_author = [
  # mainstream
  'ABC',
	'CBS',
  'CNN',
  'NBC',
	'Ezra Klein', 
  'New York Times',
  'New Yorker',
  'NPR',
  'Wall Street Journal',
  # independent
  'All In',
  'Chris Hedges',
	'Democracy Now',
	'Democracy Now Headlines',
  'Owen Jones',
	'Theo Von'
	'Lex Fridman',
	'Joe Rogan', 
	'Tucker Carlson',
  'Young Turks'
]

def rename_folder_and_files(
		old_name, 
		new_name,
		transcript_folder='_Transcripts', 
	):
	# Rename the folder
	old_folder_name = os.path.join(transcript_folder, old_name)
	new_folder_name = os.path.join(transcript_folder, new_name)
	if os.path.exists(old_folder_name):
		os.rename(old_folder_name, new_folder_name)
	
		# Rename all files within the folder
		for filename in os.listdir(new_folder_name):
			old_file_path = os.path.join(new_folder_name, filename)
			if os.path.isfile(old_file_path):
				new_file_path = os.path.join(
					new_folder_name, 
					filename.replace(old_name, new_name)
				)
				os.rename(old_file_path, new_file_path)
				print(f'Renamed: {old_file_path} to {new_file_path}')
	else:
		print(f'Folder {old_folder_name} does not exist.')

def print_all_authors():
	transcript_dir_path = '_Transcripts'
	print('All Podcasts:')
	all_authors = []
	for dir in os.listdir(transcript_dir_path):
		if os.path.isdir(os.path.join(transcript_dir_path, dir)):
			# find the file with the most recent date in the file name, sort by date and get the first one
			recent_file = sorted(os.listdir(os.path.join(transcript_dir_path, dir)), reverse=True)[0].split('_')[0]
			# convert YYYYMMDD to YYYY-MM-DD format
			recent_date = datetime.datetime.strptime(recent_file, '%Y%m%d').strftime('%Y-%m-%d')
			print(f'  {dir:>50}: {len(os.listdir(os.path.join(transcript_dir_path, dir))):<4} ({recent_date})')
			all_authors.append(dir)
	return all_authors

def find_transcripts(author_names, transcript_dir_path='_Transcripts'):
	transcript_paths_dict = defaultdict(list)
	if author_names == 'all' or author_names == ['all']:
		author_names = [dir for dir in os.listdir(transcript_dir_path) if os.path.isdir(os.path.join(transcript_dir_path, dir))]
		print(f'Finding all transcripts for {author_names}.')
	print(f'Transcript directory: {transcript_dir_path}')
	for dir in os.listdir(transcript_dir_path):
		# check if dir and if author_name is in dir
		for author_name in author_names:
			if os.path.isdir(os.path.join(transcript_dir_path, dir)) and author_name in dir:
				print(f'Loading {author_name}.')
				for file in sorted(os.listdir(os.path.join(transcript_dir_path, dir)), reverse=True):
					transcript_paths_dict[author_name].append(os.path.join(transcript_dir_path, dir, file))
				print(f' Found {len(transcript_paths_dict[author_name])} transcripts.')
	if len(transcript_paths_dict[author_name]) == 0:
		print(f'No transcripts found for {author_name}.')
		sys.exit(1)
	else:
		transcript_paths_all = [transcript for author_name, transcripts in transcript_paths_dict.items() for transcript in transcripts]
		print(f'Found {len(transcript_paths_all)} total transcripts for {author_names}.')
	return transcript_paths_dict

def extract_yaml_front_matter(f, transcript_dict):
	# default meta keys
	default_keys = [
		'Date Generated', 
		'Transcription Model', 
		'Length', 
		'Video Keywords', 
		'Video Views', 
		'Video Rating', 
		'Video Description'
	]
	# capture all the meta data until the next --- is found
	meta_data = ''
	meta_dict = defaultdict(str)
	for line in f:
		if line == '---\n':
			break
		meta_data += line
	# extract all the information with 'header' : 'value' format
	meta_data = meta_data.split('\n')
	for data in meta_data:
		if data != '' and len(data.split(': ')) == 2:
			header, value = data.split(': ')
			# check if value is an int and convert it
			try:
				value = int(value)
			except:
				pass
			meta_dict[header] = value
	# remove keys not in default_keys
	for key in list(meta_dict.keys()):
		if key not in default_keys:
			meta_dict.pop(key)
	# rename keys to lowercase and remove spaces with underscores
	for key in list(meta_dict.keys()):
		meta_dict[key.lower().replace(' ', '_')] = meta_dict.pop(key)
	return meta_dict

def read_transcript(author_name, transcript_path, transcript_dict, verbose=False):
	# deal with UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 304: character maps to <undefined> errors
	with open(transcript_path, 'r', encoding='utf-8') as f:
		if verbose:
			print(f'  Reading: {transcript_path}')
		meta_flag = False
		meta_dict = defaultdict(str)
		for line in f:
			# read the .md meta data in YAML Front Matter format --- 
			if line == '---\n' and not meta_flag:
				meta_dict = extract_yaml_front_matter(f, transcript_dict)
				meta_flag = True
			# title is the first line of the transcript, with # at the beginning
			elif line[0] == '#':
				meta_flag = False
				title = line[1:].strip()
				transcript_dict[title]['podcast'] = author_name
			# date is in the second line of the transcript, between [ and ]
			# url is in the second line of the transcript, between ( and )
			elif line[:2] == '**':
				date = re.search(r'\[(.*?)\]', line).group(1)
				# conver date to datetime (December 6, 2023 -> 2023-12-06)
				date = datetime.datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
				# add year, month, day to the dict
				year = date[:4]
				month = date[5:7]
				day = date[8:]
				transcript_dict[title]['date'] = date
				transcript_dict[title]['year'] = year
				transcript_dict[title]['month'] = month
				transcript_dict[title]['day'] = day
				transcript_dict[title]['date'] = date
				# convert date to day of the week
				weekday = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%A')
				transcript_dict[title]['weekday'] = weekday
				url = re.search(r'\((.*?)\)', line).group(1)
				transcript_dict[title]['url'] = url
			elif not meta_flag:
				# add the line to the transcript (taking out leading * and other formatting including ' and ")
				transcript_dict[title]['transcript'].append(str(line[3:].strip()))
		if len(meta_dict) > 0:
			for key, value in meta_dict.items():
				transcript_dict[title][key] = value
		# add the path to the dict
		transcript_dict[title]['path'] = transcript_path
		return transcript_dict

def dict_to_pandas(transcript_dict):
	# initialize the dataframe
	transcript_df = pd.DataFrame()
	for title, content in transcript_dict.items():
		# add the title to the content at the beginning
		content['title'] = title
		transcript_df = pd.concat([transcript_df, pd.DataFrame([content])], ignore_index=True)
	# sort by year, month, day and reset the index
	transcript_df = transcript_df.sort_values(by=['year', 'month', 'day'], ascending=False, ignore_index=True)
	# move Title to the front of the dataframe
	cols = transcript_df.columns.tolist()
	cols = cols[-1:] + cols[:-1]
	transcript_df = transcript_df[cols]
	# transcript_df['Video Views'] = transcript_df['Video Views'].str.replace(',', '').astype(int)
	return transcript_df

def pickle_transcript_df(transcript_df, save_name, dataframe_dir_path = '_Dataframes'):
	# get directory of path 
	if not os.path.exists(os.dataframe_dir_path):
		os.makedirs(dataframe_dir_path)
	df_path = os.path.join(dataframe_dir_path, save_name)
	if '.pkl' not in df_path:
		df_path += '.pkl'
	with open(df_path, 'wb') as f:
		pickle.dump(transcript_df, f)
		print(f'Pickled {df_path}.')

def dataframe_exists(author_name):
	dataframe_dir_path = '_Dataframes'
	for file in os.listdir(dataframe_dir_path):
		if author_name in file:
			return True
	return False

# rename every file in _Transcripts/<author> from <date>_* to <date>_<author>.md
def rename_files(author_name = 'Democracy Now Headlines'):
	transcript_dir_path = '_Transcripts'
	for file in os.listdir(os.path.join(transcript_dir_path, author_name)):
		if '.md' in file:
			date = file.split('_')[0]
			new_file = f'{date}_{author_name}.md'
			print(f'Renaming {file} to {new_file}.')
			os.rename(os.path.join(transcript_dir_path, author_name, file), 
						 		os.path.join(transcript_dir_path, author_name, new_file))

def add_path_var(transcript_df, var='length'):
	if var not in transcript_df.columns:
		print(f'var does not exist')
		return
	paths, length = transcript_df['path'].values, transcript_df[var].values
	# rename each file to include the length the end (remmove the .md and add it back)
	print(f'Adding {var} to file names...')
	for path, length in zip(paths, length):
		# get the file name
		path_old, ext = os.path.splitext(path)
		new_name = path_old+f'_{length}'
		os.rename(path, new_name+ext)
		print(f' {path} -> {new_name+ext}')

def load_transcripts(
		author_names = ['New York Times'], 
		reload=True, 
		save_df=False, 
		save_name='transcript_df.pkl', 
		verbose=False
	):
	# author_name = sys.argv[1]
	for author_name in author_names:
		print(f'Searching for {author_name} transcripts...')
		# check if the dataframe exists
		if dataframe_exists(author_name) and not reload:
			print(f'Found: transcript_df already exists.')
			dataframe_dir_path = os.path.join('_Dataframes', f'{author_name}_transcript_df.pickle')
			print(f'  Loading \'{dataframe_dir_path}\'...')
			with open(dataframe_dir_path, 'rb') as f:
				transcript_df = pickle.load(f)
				print(f'  Number of transcripts: {len(transcript_df)}.')
		# if the dataframe does not exist, create it by reading the transcripts
		transcript_paths_dict = find_transcripts(author_names)
		transcripts_dict = defaultdict(lambda: defaultdict(list))
		for author_name, transcripts in transcript_paths_dict.items():
			for transcript_path in transcripts:
				if '.md' in transcript_path:
					transcripts_dict = read_transcript(author_name, transcript_path, transcripts_dict, verbose)
		transcript_df = dict_to_pandas(transcripts_dict)
	if save_df:
		pickle_transcript_df(transcript_df, save_name)
	return transcript_df

