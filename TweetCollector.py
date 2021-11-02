from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tweepy
import re
import nltk
import sys
import io
import os

tweetSet = set()

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

auth = tweepy.AppAuthHandler(
    "lonV8ckyTxquyCbIff15AbHLY", "Qcda4SengqYeNhRpBFtZmFxsG0GgWhqvaXMPBO6BVxnSa7m1rF")  # Personal authorization code for Twitter interface

api = tweepy.API(auth)

# try:
api.verify_credentials()
    # print("Authentication OK")
# except:
#     print("Error during authentication")

# Set up the Tweet scraping API so that it follows rate limit
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

searchTerm = 'biden'  # Search term for twitter, can be any strig
numTweets = 1000000  # Number of tweets to pull
tweetsPerQry = 100  # How many tweets per query
fileName = 'tweets.txt'  # Where the tweets are saved

sinceId = None  # Initilization variables to allow for the scraper to remember where it left on when it reaches the rate limit
startid = -1

tweetCount = 0
print("Downloading max {0} tweets".format(numTweets))
with io.open(fileName, 'w', encoding="utf-8") as f:
    while tweetCount < numTweets:
        if (startid <= 0):
            if (not sinceId):
                new_tweets = api.search(
                    q=searchTerm, count=tweetsPerQry, tweet_mode='extended')
            else:
                new_tweets = api.search(
                    q=searchTerm, count=tweetsPerQry, since_id=sinceId, tweet_mode='extended')
        else:
            if (not sinceId):
                new_tweets = api.search(q=searchTerm, count=tweetsPerQry, startid=str(
                    startid - 1), tweet_mode='extended')
            else:
                new_tweets = api.search(q=searchTerm, count=tweetsPerQry, startid=str(
                    startid - 1), since_id=sinceId, tweet_mode='extended')
        if not new_tweets:
            break
        for tweet in new_tweets:
            try:
                string = tweet.retweeted_status.full_text
            except AttributeError:
                string = tweet.full_text

            # Stripping the strings down to plain text, removing any associated links
            stripped = re.sub(r'http\S+', '', string)
            stripped = re.sub("[@].*[' ']", "", stripped)
            stripped = stripped.rstrip()
            stripped = stripped.replace("&amp;", "&")

            # Sentiment test to filter by only negative tweets
            if (sid.polarity_scores(stripped)['compound'] < 0):
                tweetSet.add(stripped)

        tweetCount += len(new_tweets)
        print(f"Downloaded {tweetCount} tweets")
        startid = new_tweets[-1].id

    print(f"{len(tweetSet)} tweets saved to {fileName}")
    for x in tweetSet:
        f.write(f"{x}\n")

f.close()
