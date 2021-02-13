from flask import Flask, render_template, request
import feedparser
import requests
import pandas as pd
import numpy as np
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json as json
from html.parser import HTMLParser
import json

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



search_terms = ['#', '#']
def stream_tweets(search_term):
    data = [] # empty list to which tweet_details obj will be added
    counter = 0 # counter to keep track of each iteration
    for tweet in tweepy.Cursor(api.search, q='\"{}\" -filter:retweets'.format(search_term), count=100, lang='en', tweet_mode='extended').items(30):
        tweet_details = {}
        tweet_details['name'] = tweet.user.screen_name
        tweet_details['tweet'] = tweet.full_text
        tweet_details['retweets'] = tweet.retweet_count
        tweet_details['location'] = tweet.user.location
        tweet_details['created'] = tweet.created_at.strftime("%d-%b-%Y")
        tweet_details['followers'] = tweet.user.followers_count
        tweet_details['is_user_verified'] = tweet.user.verified
        data.append(tweet_details)
        
        counter += 1
        print(tweet.full_text)
        print(tweet.user.screen_name)
        print(tweet.user.location) 
stream_tweets(search_terms)






df = pd.DataFrame(columns = ['screen_name', 'text', 'location'])
print(df)

def stream(data, file_name):

    i = 0

    for tweet in tweepy.Cursor(api.search, q='iot', count=100, lang='en', tweet_mode='extended' ).items(200):

        print(i, end='\r')

        df.loc[i, 'Tweets'] = tweet.full_text

        df.loc[i, 'User'] = tweet.user.screen_name

        df.loc[i, 'User_statuses_count'] = tweet.user.statuses_count

        df.loc[i, 'user_followers'] = tweet.user.followers_count

        df.loc[i, 'User_location'] = tweet.user.location

        df.loc[i, 'User_verified'] = tweet.user.verified

        df.loc[i, 'fav_count'] = tweet.favorite_count

        df.loc[i, 'rt_count'] = tweet.retweet_count

        df.loc[i, 'tweet_date'] = tweet.created_at

        df.to_csv(('my_tweets'))

        i+=1

        if i == 200:

            break

        else:

            pass

nasty = stream(data = ['iot'], file_name = '')
print(nasty)
print(df.head())
print(df)
print(df.info())