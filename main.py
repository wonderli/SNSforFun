#!/usr/bin/env python2.7
from config import Conf 
import tweepy
if __name__ == '__main__':
    config = Conf("config")
    #config.printConf()
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    api = tweepy.API(auth)
    print api.me().name
    #api.update_status("hello world")
    l = api.home_timeline()
    last_id = config.last_id

    last = 0
    if config.last_id == '':
        last = 0
    else:
        last = int(config.last_id)

    config.last_id = l[0].id_str
    try:
        tweets = open("tweets.txt", 'a')
    except IOError:
        print "can't open %s to write" % tweets
    for e in l:
        if int(e.id_str) > last:
            tweets.write(e.author.name + ":\t" + e.text)

    config.saveConf()
        


