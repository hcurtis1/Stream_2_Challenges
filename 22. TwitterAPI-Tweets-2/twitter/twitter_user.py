import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'fNkr1J1GMAVF6KkM9qZfhxZa5'
CONSUMER_SECRET = 'C54499OUq4J6sQTkDYtNWUQFyr78ELXcmAdnE1i4Vu1HGSoGfw'
OAUTH_TOKEN = '1922806141-7HXem7A6sd5V8ciXT2Avdg3EFywTfIROoXA4ViV'
OAUTH_TOKEN_SECRET = 'tGjiKsijNvHUutRwXP8pmZ9jYnAAcZey2Y6WKEPHHpmUv'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

user = api.get_user('@FayePBoyle')

print user.screen_name
print user.followers_count

for friend in user.friends():
    print
    print friend.screen_name
    print friend.followers_count

# Harvesting tweets on user's timeline

print "------------------"
print "User's timeline below"
print "__________________"

for status in tweepy.Cursor(api.home_timeline).items(10):
    print "__________________"
    print status.text
