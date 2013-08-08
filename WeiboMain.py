#!/usr/bin/env python2.7
from WeiboConfig import WeiboConf 
from weibo import APIClient
if __name__ == '__main__':
    config = WeiboConf("weibo_config")
    config.printConf()
    client = APIClient(app_key = config.app_key, app_secret = config.app_secret, redirect_uri = config.callback_url)
    if config.access_token == '' :
        url = client.get_authorize_url() 
        print url
        config.auth_code = raw_input()
        r = client.request_access_token(config.auth_code)
        config.access_token = r.access_token
        config.expires_in = r.expires_in
    expires_in = float(config.expires_in)
    client.set_access_token(config.access_token, expires_in)
    timeline = client.statuses.friends_timeline.get()
    print timeline.__doc__
    for e in timeline.statuses:
        print "%s:\t%s" % (e.user.screen_name, e.text)

    config.saveConf()


    


    #l = api.home_timeline()
    #last_id = config.last_id

    #last = 0
    #if config.last_id == '':
    #    last = 0
    #else:
    #    last = int(config.last_id)

    #config.last_id = l[0].id_str
    #try:
    #    tweets = open("tweets.txt", 'a')
    #except IOError:
    #    print "can't open %s to write" % tweets
    #for e in l:
    #    if int(e.id_str) > last:
    #        tweets.write(e.author.name + ":\t" + e.text)

    #config.saveConf()
        


