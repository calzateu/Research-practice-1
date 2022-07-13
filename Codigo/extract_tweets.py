import os
import tweepy
from dotenv import load_dotenv


load_dotenv()

consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
bearer_token = os.environ["BEARER_TOKEN"]


client = tweepy.Client(
  bearer_token=bearer_token,
  consumer_key=consumer_key,
  consumer_secret=consumer_secret,
  access_token=access_token,
  access_token_secret=access_token_secret,
  #return_type = requests.Response,
  wait_on_rate_limit=True
)


# Search Recent Tweets
# This endpoint/method returns Tweets from the last seven days
query = 'depresión yo tengo'

# # get max. 10 tweets
# tweets = api.search_recent_tweets(
#   query=query,
#   tweet_fields=['author_id', 'created_at'],
#   max_results=10
# )

# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
response = client.search_recent_tweets(query=query, max_results=100)
print(response.meta)


# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

print(tweets)

# Each Tweet object has default ID and text fields
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)