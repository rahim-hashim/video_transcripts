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

search_term = 'all' # 'all', 'news_author', 'last_5', or 'New York Times'

transcript_df = load_transcripts(
  search_term, 
  save_name='transcript_df.pkl', 
  reload=True,
  save_df=True
)


# ***
# ## Explore Dataset

# In[4]:


# reverse the order of the x-axis
# show all columns
pd.set_option('display.max_columns', None)
transcript_df = transcript_df.sort_values(
	by=['date', 'video_views'], 
	ascending=False, 
	ignore_index=True
)
transcript_df


# ***
# ## Search Topics

# ### Recent Podcasts

# In[ ]:


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
topics = ['Israel', 'Palestine']
recent_df = count_recent_mentions(transcript_df, topics, recent_days)


# In[11]:


recent_topic_df = recent_df[recent_df['total_count'] > 0].copy()
# sort by total_count
recent_topic_df = recent_topic_df.sort_values(by='total_count', ascending=False, ignore_index=True)
recent_topic_df


# In[16]:


# print all urls where the topic is mentioned
recent_topic_df['text'] = recent_topic_df['transcript']
for topic in topics:
	press_releases.print_topic_segments(
		recent_topic_df, 
		topic, 
		max_print=10, 
		most_recent_dates=5
	)


# #### Generate Topic Dataframe

# In[ ]:


def generate_topic_df(transcript_df, topics, text_field='transcript'):
	if type(transcript_df[text_field].iloc[0]) == list:
		transcript_df = transcript_df.explode('transcript', ignore_index=True)
		transcript_df['position'] = transcript_df.groupby('title').cumcount()
	# initialize topic_df
	topic_df = pd.DataFrame()

	for podcast in transcript_df['podcast'].unique():
		print(podcast)
		for topic in topics:
			print(f'  Topic: {topic}')
			podcast_topic_df = press_releases.count_topic_mentions(
				transcript_df[transcript_df['podcast'] == podcast], 
				topic, 
				search_field='transcript', 
				verbose=False
			)
			topic_df = pd.concat([topic_df, podcast_topic_df], ignore_index=True)
		# count total number of unique podcasts with any topic mentions
		print('-----------------------------')
	return topic_df

topic_df = generate_topic_df(transcript_df, topics)


# In[45]:


# sort by topic_url_count, url, and date
topic = topics[0]
# create a new column adding up the total topic counts
topic_cols = [col for col in topic_df.columns if 'url_count' in col]
topic_df['all_url_count'] = topic_df[topic_cols].sum(axis=1)
topic_df['all_url_count_rate'] = topic_df[topic_cols].sum(axis=1)/topic_df['length_time']


# In[46]:


topic_df = topic_df[topic_df['all_url_count'] > 0]
topic_date_df = topic_df.drop_duplicates(subset=['url']).sort_values(
	# by=[f'all_url_count_rate', 'url', 'date'], 
  by=['date', f'all_url_count', 'url'],
	ascending=False).reset_index()[['podcast', 'title', 'date', 'all_url_count', 'all_url_count_rate', 'video_views', 'length',  'url']]
topic_date_df.head(15)


# In[ ]:


# print all urls where the topic is mentioned
topic_df['text'] = topic_df['transcript']
press_releases.print_topic_segments(
	topic_df, 
	topic, 
	max_print=10, 
	most_recent_dates=5
)


# ***
# ## Example 1: News Middle Eastern Coverage
# 
# We can look across multiple podcasts and news coverages to search for a specific topic.

# In[9]:


import numpy as np
def plot_topics(podcast, df, topics):
	df['datetime'] = pd.to_datetime(df['date'])
	df['month_year'] = df['datetime'].dt.to_period('M')
	plt.figure(figsize=(12, 4))
		# get all months between the first and last month
	months = list(map(str, pd.period_range(start=df['month_year'].min(), 
																					end=df['month_year'].max(), 
																					freq='M')))
	for topic in topics:
		print(f'Topic: {topic}')
		topic_df = press_releases.count_topic_mentions(
			topic=topic, 
			transcript_df=df, 
			search_field='transcript', 
			verbose=False
		)
		# see if topic_df is None or empty
		if topic_df is None or len(topic_df) == 0:
			# plot 0 for all months
			months_count = [0] * len(months)
			plt.plot(months, months_count, label=topic, lw=2.5)
		# count the number of times the topic is mentioned in each month
		else:
			months_count = []
			for month in months:
				month_df = topic_df[topic_df['month_year'] == month]
				if len(month_df) == 0:
					month_url_count = 0
				else:
					# get unique urls and sum the counts for each url
					month_url_count = 0
					for url in month_df['url'].unique():
						month_url_count += month_df[month_df['url'] == url][f'{topic}_url_count'].iloc[0]
				months_count.append(month_url_count)
				print(f'    {month:<4}: {round(month_url_count,2)}')
			plt.plot(months, months_count, label=topic, lw=2.5)
	plt.xticks(rotation=45)
	title=f'{podcast} - Number of Mentions'
	plt.title(title)
	plt.legend()

topics=['Israel', 'Palestine', 'China', 'Japan', 'Russia', 'Ukraine', 'Iran', 'North Korea', 'Cuba', 'Canada', 'Mexico']
for podcast in transcript_df_sep['podcast'].unique():
	print(f'Podcast: {podcast}')
	plot_topics(podcast, transcript_df_sep[transcript_df_sep['podcast'] == podcast], topics)


# #### Fuzzy Search

# In[7]:


from utils.transcript_search import fuzzy_search
# perform fuzzy match for all words in target_word_list
target_word_list = ['Gaza', 'West Bank', 'Palestine', 'Israel', 'Jerusalem', 'Hamas', 'Fatah', 'Netanyahu']
topic_df = fuzzy_search(transcript_df, target_word_list, fuzzy_threshold=0.85)

# sort by video_views
print(f'Number of transcripts: {len(topic_df)}')
topic_df = topic_df.sort_values(by='video_views', ascending=False, ignore_index=True)
topic_df[topic_df['max_fuzzy_Israel'] > 0.9]


# #### Analysis

# In[22]:


# make a scatter plot for each date whether the target words are in the transcript
sns.set_style("ticks")
plt.figure(figsize=(30, 4))
dates = topic_df['date']
# colormap for all dates
colors = sns.color_palette('tab10', n_colors=len(target_word_list))
titles = []
for date in tqdm.tqdm(sorted(dates), desc='Dates'):
		date_df = topic_df[topic_df['date'] == date]
		for idx, word in enumerate(target_word_list):
			if date_df[f'max_fuzzy_{word}'].max() > 0.9:
				plt.scatter(date, 10-idx, color=colors[idx], s=30, alpha=0.5, label=word)
				titles.append(date_df['title'].values[0])
plt.xticks(rotation=90, fontsize=8)
# make xticklabels the titles
plt.gca().set_xticklabels(titles)
plt.title(f'{author_names} Topic Search')
# only show the legend for each word once, not for each date
# get the handles and labels for the legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc='upper left', fontsize=8)
plt.grid()
plt.tight_layout()
plt.show()


# ***
# ## Example 2: Bill Simmons - NBA Teams

# In[69]:


bs_podcast_name = ['Bill Simmons']
bs_df = load_transcripts(bs_podcast_name)


# In[70]:


bs_df


# In[71]:


from utils.transcript_search import fuzzy_search
# perform fuzzy match for all words in target_word_list
target_word_list = ['lakers', 'clippers', 'warriors', 'suns', 'kings',
                    'mavericks', 'rockets', 'grizzlies', 'pelicans', 'spurs',		
                    'timberwolves', 'thunder', 'nuggets', 'jazz', 'blazers',
								 		'heat', 'magic', 'wizards', 'hawks', 'hornets', 'nets', 
                    'celtics', 'knicks', '76ers', 'bucks', 'pacers', 
                    'pistons', 'bulls', 'cavaliers', 'raptors']
fuzzy_threshold = 0.9
bs_df = fuzzy_search(bs_df, target_word_list, fuzzy_threshold)


# In[74]:


team_colors = {
    'lakers': 	 		'#552583',  # Purple and Gold
    'clippers':  		'#C8102E',  # Red and Blue
    'warriors':  		'#1D428A',  # Royal Blue and Gold
    'suns': 		 		'#1D1160',  # Purple, Orange, and Black
    'kings': 		 		'#5A2D81',  # Purple, Silver, and Black
    'mavericks': 		'#007DC5',  # Royal Blue, Navy Blue, and Silver
    'rockets': 	 		'#CE1141',  # Red and Silver
    'grizzlies': 		'#5D76A9',  # Navy Blue, Beige, and Slate Blue
    'pelicans':  		'#0C2340',  # Navy Blue, Gold, and Red
    'spurs': 				'#C4CED4',  # Silver, Black, and White
    'timberwolves': '#0C2340',  # Navy Blue, Lake Blue, and White
    'thunder': 			'#007AC1',  # Blue, Orange, and Yellow
    'nuggets': 			'#0E2240',  # Navy Blue, Gold, and Sky Blue
    'jazz': 				'#002B5C',  # Navy Blue, Gold, and Green
    'blazers': 			'#E03A3E',  # Red, Black, and White
    'heat': 				'#98002E',  # Red, Black, and White
    'magic': 				'#0077C0',  # Royal Blue, Silver, and Black
    'wizards': 			'#002B5C',  # Navy Blue, Red, and Silver
    'hawks': 				'#E03A3E',  # Red, Black, and Silver
    'hornets': 			'#1D1160',  # Purple, Teal, and White
    'nets': 				'#000000',  # Black and White
    'celtics': 			'#007A33',  # Green and White
    'knicks': 			'#006BB6',  # Royal Blue, Orange, and Silver
    '76ers': 				'#006BB6',  # Royal Blue, Red, and White
    'bucks': 				'#00471B',  # Hunter Green, Cream, and White
    'pacers': 			'#002D62',  # Navy Blue, Gold, and White
    'pistons': 			'#C8102E',  # Red, Blue, and White
    'bulls': 				'#CE1141',  # Red, Black, and White
    'cavaliers': 		'#860038',  # Wine, Gold, and Navy Blue
    'raptors': 			'#CE1141'  	# Red, Black, and Silver
}

sns.set_theme(style="whitegrid")
plt.figure(figsize=(len(target_word_list), 5))

# for each host find the number of rows with max_fuzzy > 0.9 and plot
num_mentions_all = []
for t_idx, team in enumerate(target_word_list):
	# find the number of rows with max_fuzzy > 0.9 for the host
	nba_df = bs_df[bs_df[f'max_fuzzy_{team}'] > 0.9]
	team_mentions = nba_df.shape[0]/len(bs_df)
	num_mentions_all.append(team_mentions)

# sort the target_word_list by the number of shows mentioned
sorted_target_word_list = [x for _, x in sorted(zip(num_mentions_all, target_word_list), reverse=True)]
num_mentions_all = sorted(num_mentions_all, reverse=True)
# sort colors by the sorted target_word_list 
team_colors = {key: team_colors[key] for key in sorted_target_word_list}

plt.bar(range(len(target_word_list)), num_mentions_all, color=team_colors.values(), alpha=0.7, edgecolor='black', linewidth=2)
plt.ylim(0, 0.5)
plt.xticks(range(len(sorted_target_word_list)), sorted_target_word_list)
plt.yticks([0, 0.25, 0.5], ['0', '25%', '50%'])
# rotate the x-axis labels
plt.xticks(rotation=45, ha='right')
plt.ylabel('Percent Mentioned', fontsize=14, fontweight='bold')
plt.suptitle(f'{bs_podcast_name[0]} Podcast: NBA Teams Mentioned', fontsize=16, fontweight='bold')
# convert to mm/DD/YYYY
first_date = datetime.datetime.strptime(transcript_df['date'].iloc[-1], '%Y-%m-%d').strftime('%m/%d/%Y')
last_date = datetime.datetime.strptime(transcript_df['date'].iloc[0], '%Y-%m-%d').strftime('%m/%d/%Y')
plt.title(f'{first_date} — {last_date} (n={len(transcript_df)})', fontsize=15)
# reduce distance between sup and title
# only keep horizontal grid
plt.grid(axis='x')
# tight layout
plt.tight_layout()


# In[ ]:




