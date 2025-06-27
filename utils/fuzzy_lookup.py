# levenshtein ratio adapted from Francisco Javier Carrera
# Source: https://www.datacamp.com/community/tutorials/fuzzy-string-python

import re
import string
import numpy as np
from collections import defaultdict, Counter

def get_bigram(segment):
	bigrams = []
	for index, word in enumerate(segment):
		if index == len(segment) - 1:
			break
		# strip all punctuation from the segment
		n_1 = segment[index].translate(str.maketrans('', '', string.punctuation))
		# get the next word
		n2 = segment[index + 1].translate(str.maketrans('', '', string.punctuation))
		# add the bigram to the list
		bigrams.append(n_1 + ' ' + n2)
	return bigrams

# same function as get_bigram but for n-grams
def get_ngram(segment, n):
	ngrams = []
	if len(segment) < n:
		return ngrams
	for index, word in enumerate(segment):
		if index == len(segment) - n:
			break
		# strip all punctuation from the segment
		ngram = ''
		for i in range(n):
			ngram += segment[index + i].translate(str.maketrans('', '', string.punctuation)) + ' '
		# add the ngram to the list
		ngrams.append(ngram.strip())
	return ngrams

def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
	""" levenshtein_ratio_and_distance:
			Calculates levenshtein distance between two strings.
			If ratio_calc = True, the function computes the
			levenshtein distance ratio of similarity between two strings
			For all i and j, distance[i,j] will contain the Levenshtein
			distance between the first i characters of s and the
			first j characters of t
	"""
	# Initialize matrix of zeros
	rows = len(s)+1
	cols = len(t)+1
	distance = np.zeros((rows,cols),dtype = int)

	# Populate matrix of zeros with the indeces of each character of both strings
	for i in range(1, rows):
		for k in range(1,cols):
			distance[i][0] = i
			distance[0][k] = k

	# Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
	for col in range(1, cols):
		for row in range(1, rows):
			if s[row-1] == t[col-1]:
				cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
			else:
				# In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
				# the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
				if ratio_calc == True:
					cost = 2
				else:
					cost = 1
			distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
														distance[row][col-1] + 1,          # Cost of insertions
														distance[row-1][col-1] + cost)     # Cost of substitutions
	if ratio_calc == True:
		# Computation of the Levenshtein Distance Ratio
		# deal with the edge case where the length of the string is 0
		if len(s) == 0 or len(t) == 0:
			Ratio = 0
		else:
			Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
		return Ratio
	else:
		# print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
		# insertions and/or substitutions
		# This is the minimum number of edits needed to convert string a to string b
		return "The strings are {} edits away".format(distance[row][col])

def fuzzy_matching(target_word, segments, fuzzy_threshold=0.8):
	'''Fuzzy matching for players while requesting from html'''
	fuzzy_matches = defaultdict(lambda: defaultdict(list))
	max_fuzzy = [0, None]  # [score, name]
	target_word_size = len(target_word.split())
	# split segments into n-grams
	for idx, segment in enumerate(segments):
		segment_words = segment.split()
		# get the n-grams
		ngrams = get_ngram(segment_words, target_word_size)
		# perform fuzzy matching on the bi-grams
		for ngram in ngrams:
			fuzzy_ratio = levenshtein_ratio_and_distance(target_word.lower(), ngram.lower(), ratio_calc=True)
			if fuzzy_ratio > max_fuzzy[0]:
				max_fuzzy = [fuzzy_ratio, ngram]
			# if above a threshold, stop looking for the word
			if max_fuzzy[0] >= fuzzy_threshold:
				break
	# align the target word, match score and the segment print using fstring
	print(f'  {target_word:<20} Match Score: {round(max_fuzzy[0], 4):<6} | Match: {max_fuzzy[1]}')
	return (max_fuzzy[0], max_fuzzy[1])