import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter


CONSUMER_KEY = 'fNkr1J1GMAVF6KkM9qZfhxZa5'
CONSUMER_SECRET = 'C54499OUq4J6sQTkDYtNWUQFyr78ELXcmAdnE1i4Vu1HGSoGfw'
OAUTH_TOKEN = '1922806141-7HXem7A6sd5V8ciXT2Avdg3EFywTfIROoXA4ViV'
OAUTH_TOKEN_SECRET = 'tGjiKsijNvHUutRwXP8pmZ9jYnAAcZey2Y6WKEPHHpmUv'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 150
query = "Ireland"

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_tweets = 10  # The min amount of times a status is retweeted to gain entry to our list.
                 # Reset this value to suit your own tests

pop_tweets = [ status
               for status in results
                    if status._json['retweet_count'] > min_tweets]

tweet_tups = [(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count'])
              for tweet in pop_tweets]

# Sort the tuple entries in descending order
most_popular_tups = sorted(tweet_tups, key=itemgetter(1), reverse=True)[:5]

# Prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in most_popular_tups:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = 'l', 'r' # align columns
print table
