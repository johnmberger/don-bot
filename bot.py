import tweepy
import markovify
import re

#Twitter API credentials
consumer_key = "xxxx"
consumer_secret = "xxxx"
access_key = "xxxx"
access_secret = "xxxx"


def go_twitbot_go(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method

	# authenticate to twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

    outtweets = ''

    for tweet in alltweets:
        outtweets += tweet.text + ' '

    # strip urls
    outtweets = re.sub(r"http\S+", "", outtweets, flags=re.MULTILINE)

    text_model = markovify.Text(outtweets)
    tweet = text_model.make_short_sentence(140)
    print(tweet)
    api.update_status(tweet)

go_twitbot_go("realDonaldTrump")
