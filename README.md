# DonBot

This TwitterBot uses Natural Language Processing (which calculates probability distribution of speech output) and tweets like Donald Trump. 

Simple breakdown of how this works:
- Using [Tweepy](http://www.tweepy.org/), grab a huge chunk of Donald Trump's ([@realDonaldTrump](https://twitter.com/realDonaldTrump)) tweets
- Smash them all into a large text string
- Remove url links
- Using [Markovify](https://github.com/jsvine/markovify), build Markov models of DJT's tweets, and generate random tweets from that

This code could be adapted to imitate any other twitter user by changing the argument in the `go_twitbot_go()` function declaration
