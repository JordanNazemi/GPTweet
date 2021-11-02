This is code to develop a new model that will generate fake tweets that are either positive or
negative sentiment about a given topic. I developed this to illustrate how easy fake accounts were able to twist
the online political conversation. My pre-trained model allows for fake "negative" Tweets to be generated about 
President Joe Biden. The tweets are collected using TweePy and the model is generated using GPT-2.

REQUIRES PYTHON VERSION 3.6.8 TO RUN!

Recommended to setup and activate virtual environment before installing requirements using
"pip install -r requirements.txt"

TWEETCOLLECTOR
This program is used to collect tweets from Twitter using Tweepy and a given search term. It then saves unique tweets to a set which is 
then evaluated using Vader from NLTK to use only negative-scoring tweets. It then saves the remaining tweets into a .txt document.

Set the desired search term and tweet quantity and run from console using 
"python TweetCollector.py"

MODELBUILDER
The model builder is the way you can generate your own model from a corpus made during TweetCollector. By default you DONT need to run this
and can just use to pre-generated model.

GENERATOR
This generates tweets based on either the default model (355M model built with negative Biden tweets)

The results of this generator (and the reason for developing it) are in the GPTweet.pdf report attached to the repository.