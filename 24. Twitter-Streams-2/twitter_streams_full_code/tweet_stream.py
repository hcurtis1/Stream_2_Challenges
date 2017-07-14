from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'fNkr1J1GMAVF6KkM9qZfhxZa5'
CONSUMER_SECRET = 'C54499OUq4J6sQTkDYtNWUQFyr78ELXcmAdnE1i4Vu1HGSoGfw'
OAUTH_TOKEN = '1922806141-7HXem7A6sd5V8ciXT2Avdg3EFywTfIROoXA4ViV'
OAUTH_TOKEN_SECRET = 'tGjiKsijNvHUutRwXP8pmZ9jYnAAcZey2Y6WKEPHHpmUv'

keyword_list = ['python', 'java', 'c#', 'ruby'] # Track list

class MyStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('twitter_streams/tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    def on_error(self, status):
        print status
        return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)
