import os
import re
import sys
import tqdm
import pickle
import datetime
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
from utils import fuzzy_lookup
import matplotlib.pyplot as plt
from collections import defaultdict
# Add dimag path to the system path
sys.path.append('C:/Users/rahim/Documents/GitHub/dimag') # PC
sys.path.append('/Users/rahimhashim/Desktop/News/dimag') # Mac
# turn off warnings
warnings.filterwarnings('ignore')
import press_releases
# Add other functions
from utils.transcript_search import *

# print all the different authors
search_term = 'all' # 'all', 'news_author', 'last_5', or 'New York Times'

transcript_df = load_transcripts(
  search_term, 
  save_name='transcript_df.pkl', 
  reload=True,
  save_df=False
)

# reverse the order of the x-axis
# show all columns
pd.set_option('display.max_columns', None)
transcript_df = transcript_df.sort_values(
	by=['date', 'video_views'], 
	ascending=False, 
	ignore_index=True
)

# search for topics
from utils.search_topics import mena_topics
import textwrap

# go through transcript_df['transcript'] for each topic and count the number of times it appears but vectorize it
def count_recent_mentions(transcript_df, topics, recent_days):
	'''
	Count the number of times each topic appears in the transcript_df for the last recent_days days.

	Args:
		transcript_df (pd.DataFrame): DataFrame containing the transcripts and metadata.
		topics (list): List of topics to search for in the transcripts.
		recent_days (int): Number of days to look back

	Returns:
		pd.DataFrame: DataFrame with additional columns for each topic count and total count.
	'''
	print(f'Topics: {topics}')
	# create a copy of transcript_df headers with no rows
	current_date = datetime.datetime.now()
	start_date = current_date - datetime.timedelta(days=recent_days)
	transcript_df['date'] = pd.to_datetime(transcript_df['date'])
	print(f'Total transcripts found:  {len(transcript_df):>7}')
	# filter transcript_df for rows where date is between start_date
	recent_df = transcript_df.loc[
		(transcript_df['date'] >= start_date) &
		(transcript_df['date'] <= current_date)
	]
	print(f'Transcripts in last {recent_days} days: {len(recent_df)}')
	# for each topic count the number of times it appears in
	for index, row in recent_df.iterrows():
		for topic in topics:
			transcript = ' '.join([item.split('[[')[0].strip().lower() for item in row['transcript']])
			count = 0
			if topic.lower() in transcript:
				count = 1
			recent_df.at[index, f'{topic}_count'] = int(count)
		total_count = int(sum([recent_df.at[index, f'{topic}_count'] for topic in topics]))
		recent_df.at[index, 'total_count'] = total_count
		if total_count > 0:
			print(f'{row["podcast"][:30]:<30} | {row["date"].date()} | {total_count:>3} | {row["url"]:<45} | {row["video_description"]}')
		# convert all '{topic}_count' columns to int
	topic_cols = [col for col in recent_df.columns if '_count' in col]
	recent_df[topic_cols] = recent_df[topic_cols].apply(lambda x: x.astype(int))
	return recent_df

recent_days = 10
topics = mena_topics
# topics = ['Israel', 'Palestine']
recent_df = count_recent_mentions(transcript_df, topics, recent_days)
recent_topic_df = recent_df[recent_df['total_count'] > 0]
# sort by total_count
recent_topic_df = recent_topic_df.sort_values(by='date', ascending=False, ignore_index=True)

def explode_df(transcript_df, topics, text_field='transcript'):
	if type(transcript_df[text_field].iloc[0]) == list:
		transcript_df = transcript_df.explode(text_field, ignore_index=True)
		transcript_df['position'] = transcript_df.groupby('title').cumcount()
	return transcript_df

# print all urls where the topic is mentioned
recent_topic_df = explode_df(recent_topic_df, topics)


def print_topic_segments(
		transcript_df, 
		topics, 
		max_print=5,
		most_recent_dates=10,
		text_field='text',
	):
	'''
	Print all segments containing the specified topic and up to 
	max_print number of segments after.

	Parameters:
		topic_df (pd.DataFrame): the dataframe of press transcripts containing the topic
		topic (str): the topic to search for in the transcripts
		max_print (int): the maximum number of segments to print after the topic segment
		most_recent_dates (int): the number of most recent dates to print

	Returns:
		None

	Example:
		>>> topic_df = find_topic('economy', transcript_df)
		>>> print_topic_segments(topic_df, 'economy', max_print=5)
		...
	'''
	print(f'Printing segments mentioning \'{topics}\'...')
	topic_df = transcript_df[transcript_df[f'total_count'] >= 1].sort_values(by=['url', 'date', 'position'], ascending=[False, False, True])
	print(f'  Number of Dates: {len(topic_df["date"].unique())}\n')
	for d_index, date in enumerate(sorted(topic_df['date'].unique(), reverse=True)):
		date_df = topic_df[topic_df['date'] == date]
		for url in date_df['url'].unique():
			podcast = date_df[date_df['url'] == url]['podcast'].iloc[0]
			url_df = date_df[date_df['url'] == url]
			title = url_df.iloc[0]['title']
			print(f'{podcast}: {title}')
			print(f'  {date}: ({url})')
			print(f'  {url_df.iloc[0]["path"]}')
			print(f'  {url_df.iloc[0]["video_description"]}')
			# print number of mentions
			print(f'  Mentions: {url_df[f"total_count"].iloc[0]}')
			positions_printed = []
			for index, row in url_df.iterrows():
				# get the topic(s) in the text
				topics_included = []
				for topic in topics:
					if topic.lower() in row[text_field].lower():
						timestamp = '[' + row[text_field].split('[[')[1]
						position = row['position']
						if position in positions_printed:
							continue
						print(f'  [{topic}: {timestamp}]')
						positions_printed.append(position)
						text_stripped = row[text_field].split('[[')[0].strip()
						print(textwrap.fill(f'  -> {row["position"]:<4} | {(text_stripped)}', width=200, subsequent_indent=' '*39))
						# print the next max_print segments after the topic segment
						for i, row in url_df.iterrows():
							if row['position'] > position and row['position'] < position + max_print:
								text_stripped_subsequent = row[text_field].split('[[')[0].strip()
								print(textwrap.fill(f'     {row["position"]:<4} | {(text_stripped_subsequent)}', width=200, subsequent_indent=' '*39))
								positions_printed.append(row['position'])
						print('  '+'-'*200)
		
		if most_recent_dates and d_index > most_recent_dates:
			return

print_topic_segments(
	recent_topic_df, 
	topics, 
	max_print=10, 
	most_recent_dates=5,
	text_field='transcript',
)