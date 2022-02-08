import os
import random
import json
from pathlib import Path
import tweepy
import csv

ROOT = Path(__file__).resolve().parents[0]
tweets = []
tweets_file = ROOT / "tweets.csv"
with open(tweets_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tweets.append(row['Lines'])


def lambda_handler(event, context):
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    name = "TheDarKnightBot"
    id = api.get_user(screen_name=name)
    tweet = tweets[id.statuses_count] + \
        " (" + str(id.statuses_count+1) + "/3027) "
    print(tweet)
    api.update_status(tweet)
    return {"statusCode": 200, "tweet": tweet}
