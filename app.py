import os
import settings
import twitter

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN_KEY = os.environ.get('ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

print CONSUMER_KEY

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN_KEY,
                  access_token_secret=ACCESS_TOKEN_SECRET,)

def get_tweets(count):
    tflns = api.GetUserTimeline(user_id=21506437, count=count)
    return tflns

for status in get_tweets(100):
    if status.text[0] == "(":
        print status.text, '\n'