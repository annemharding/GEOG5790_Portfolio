# -*- coding: utf-8 -*-
"""
Anne Harding, 14/03/2019
GEOG5790 - Practical 8 (NLTK)
Script to tokenise example text file.
"""
# -----------------------------------------------------------
# Import modules:
import nltk
import copy

# Download nltk packages:
# Only need to run once!
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# -----------------------------------------------------------
# READ IN TEXT FILE AND TRIM DOWN:

# Read in .txt file of The Wasteland by T.S. Elliott
f = open("1321-0.txt", encoding="utf8")
text = f.read()
# Close .txt file:
f.close()

# Print out whole variable to check read in properly:
# print(text)

# Print out variable line-by-line:
# for line in text:
#     print(line)
    
# Trim down:
# Identify words at start point:
start =  "“Nam Sibyllam quidem Cumis ego ipse oculis meis"
# Identify words at end point:
end = "Line 415 aetherial] aethereal"
# Find location of start point:
start_pos = text.find(start)
# Find location of end point:
end_pos = text.find(end)
# Trim text between start point and end point:
text = text[start_pos:end_pos]
# Check text has been trimmed down properly by printing:
# print(text)

# Tokenise the raw text:
tokens = nltk.word_tokenize(text)
# Convert into an nltk.Text object:
text = nltk.Text(tokens)
# Number of words:
print(len(text))

# ------------------------------------------------------------------------
# SIMPLE ANALYSES:
# 20 most common words:
# Create frequency distribution of words:
fdist = nltk.FreqDist(text)
# Print 20 most common words:
print(fdist.most_common(20))
# Frequency distribution plot:
fdist.plot(50, cumulative=True)
# This list contains punctuation instances as words (e.g. ',', ''', '?')
# Punctuation does not count as a word, therefore I need to remove any
# punctuation instances from the most common words.

# Create a deep copy of fdist so that I can remove words without encountering
# an error saying that the dictionary being looped over is changing size:
fdist_temp = copy.deepcopy(fdist)
# Print "HERE" to be able to identify more easily in the console print-out:
print("HERE")
print(fdist_temp.values)

# Loop through words in fdist:
for word in fdist:
    # If word does not contain completely alphanumeric characters:
    if word.isalnum() == False:
        # If length of word is 1 character:
        if len(word) == 1:
            # Print word to check:
            print(word)
            # Remove word from fdist_temp:
            fdist_temp.pop(word)
# Print values in fdist_temp to check that this has worked:
# print(fdist_temp.values)
# 20 most-common words used (NOT INCLUDING PUNCTUATION):
print(fdist_temp.most_common(20))
# Frequency distribution plot:
fdist_temp.plot(50, cumulative=True)

# 20 most common word lengths:
fdist =  nltk.FreqDist(len(w) for w in text)
print(fdist.most_common(20))

# All words over 10 letters long:
long_words = [w for w in text if len(w) > 10]
print(long_words)
print(len(long_words))

# ------------------------------------------------------------------------
# SPEECH-TAGGING:
# Tag all:
tagged = nltk.pos_tag(text) 
# Print tagged list to check:
print(tagged)
'''
# METHOD OF TAGGING ONLY NNP VALUES WHICH DID NOT WORK:
# Tag only NNP:
# tagged_nnp = nltk.pos_tag(text, tagset='NNP == Proper nouns')
tagged_nnp = nltk.pos_tag(text, tagset='NNP')
# Print tagged_nnp list to check:
print(tagged_nnp)
'''
# Create empty list:
tagged_nnp = []
# Loop through tagged list of tuples:
for tag in tagged:
    # If tag tuple is 'NNP':
    if tag[1] == 'NNP':
        # Print to screen for manual check:
        print(tag)
        # Append tag tuple to new list:
        tagged_nnp.append(tag)
# Print list of tuples with 'NNP' tag to check:
print(tagged_nnp)

# Create empty list:
proper_nouns = []

# Loop through words in tagged_nnp:
for tag in tagged_nnp:
    # If word contains completely alphanumeric characters:
    if tag[0].isalnum() == True:
        # Print word to check:
        print(tag)
        # Append word to proper_nouns list:
        proper_nouns.append(tag)

# Convert from list of tuples to list (i.e. remove tag):
proper_nouns = [tag[0] for tag in proper_nouns]

# Print statement to check final output:
print("FINAL LIST OF PROPER NOUNS HERE:")
print(proper_nouns)

# ------------------------------------------------------------
# GOOGLE API GEOCODING:
import time
import requests

# Define Google API URL:
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
# Get API Key:
with open ('api.txt') as f:
    API_KEY = f.readline().strip()
# Print API_KEY to check manually:
# print(API_KEY)

# Find location of "Leicester" in proper_nouns list for example:
index = proper_nouns.index('Leicester')
print("Index of 'Leicester' is: " + str(index)) # 222

for noun in proper_nouns[222:223]:
    # Use print statement to check:
    print(noun)
    # Create params dictionary:
    params = {
            'address': noun,    # set address as proper noun
            'region': 'uk',     # set region as UK
            'key': API_KEY}     # provide API key
    # Request:
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    # Pause for 0.5 seconds:
    time.sleep(0.5)
    # Results:
    res = req.json()
    # Print res to check manually:
    print(res)
    
    if res['results']:
        # Use the results:
        result = res['results'][0]
        # Print result to check manually:
        # print(result)
        
        # Define geodata:
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        
        # Print formatted result as lat, long:
        print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
    
    else:
        print("No results.")
