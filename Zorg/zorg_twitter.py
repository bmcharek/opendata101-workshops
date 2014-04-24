#!/usr/bin/env python

# from twitter import Api, Twitter
"""
create twitter app and get tokens
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
virtual_env .
source bin/activate
easy_install python-dateutil
./participatie_twitter.py
"""

from TwitterAPI import TwitterAPI

consumer_key = "xxxxxxxxxx"
consumer_secret = "xxxxxxxxxx"
access_token_key = "xxxxxxxxxx"
access_token_secret = "xxxxxxxxxx"

from twython import Twython
APP_KEY = consumer_key
APP_SECRET = consumer_secret
OAUTH_TOKEN = access_token_key
OAUTH_TOKEN_SECRET = access_token_secret

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-m", "--module", dest="modulename",
                  help="specify you MODULE", metavar="MODULE",  default="rw_tweets")
(options, args) = parser.parse_args()


def rw_tweets():
    import tweepy
    import csv #Import csv
    from datetime import date, timedelta
    #Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)
    # Open/Create a file to append data
    csvFile = open('result.csv', 'a')
    #Use csv Writer
    results = []
    retweets = []
    words_to_remove = """met sommige jou de het een """

    since = date.today()-timedelta(days=1)
    until = date.today()
    geocode = None #'52.36,4.94,10km',
    lang = 'nl'
    result_type = None #'popular'

    #Watch out doesn't remove old data
    #for fresh file, rm old file
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['Datum', 'Tweet'])
    query = "zorg"
    for tweet in tweepy.Cursor(api.search,
                               q=query,
                               since=since,
                               until=until,
                               geocode=geocode,
                               result_type= result_type,
                               lang=lang).items():
        #Write a row to the csv file/ I use encode utf-8
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        # import pdb
        # pdb.set_trace()
        if tweet.retweet:
            retweets.append(tweet)
        else:
            results.append(tweet)
        # print tweet.created_at, tweet.text
    csvFile.close()

    # Quick summary
    print 'query:   ', query
    print 'results: ', len(results)
    print 'retweets:', len(retweets)
    print 'Variable `tweets` has a list of all the tweet texts'
    # import pdb
    # pdb.set_trace()
    tweets = [t.text for t in retweets]
    print tweets[:10]

if __name__ == '__main__':
    if options.modulename == "rw_tweets":
        rw_tweets()
