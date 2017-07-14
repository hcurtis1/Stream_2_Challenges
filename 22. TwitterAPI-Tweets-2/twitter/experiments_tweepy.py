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

for status in tweepy.Cursor(api.user_timeline, id="@FayePBoyle").items(10):
    print "__________________"
    print status.text

# To enable a new follower
def make_new_pal(palerino):
    api.create_friendship(str(palerino))
    print "You've started following %s!" % str(palerino)

make_new_pal("@louistheroux")


# To stop following user

def forget_you_pal(palerino):
    api.destroy_friendship(str(palerino))
    print "You've stopped following %s" % str(palerino)

forget_you_pal("@louistheroux")

# To send out a tweet

def new_tweet(my_tweet):
    api.update_status(str(my_tweet))
    print "You've updated your status with the following: %s" % str(my_tweet)

new_tweet("Sending out my first tweet using the Twitter API! (Hope this works)")