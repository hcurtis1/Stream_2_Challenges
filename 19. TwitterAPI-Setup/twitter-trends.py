import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'fNkr1J1GMAVF6KkM9qZfhxZa5'
CONSUMER_SECRET = 'C54499OUq4J6sQTkDYtNWUQFyr78ELXcmAdnE1i4Vu1HGSoGfw'
OAUTH_TOKEN = '1922806141-7HXem7A6sd5V8ciXT2Avdg3EFywTfIROoXA4ViV'
OAUTH_TOKEN_SECRET = 'tGjiKsijNvHUutRwXP8pmZ9jYnAAcZey2Y6WKEPHHpmUv'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

lon_trends = api.trends_place(LON_WOE_ID)
dub_trends = api.trends_place(DUB_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print common_trends
print json.dumps(lon_trends, indent=1)
