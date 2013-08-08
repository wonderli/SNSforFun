#!/usr/bin/env python2.7
import os
class WeiboConf(object):
    def __init__(self, filename):
        self.app_key=""
        self.app_secret=""
        self.callback_url=""
        self.filename = filename
        self.last_id = ""
        self.auth_code=""
        self.access_token=""
        self.expires_in=""
        self.readConf()
    def readConf(self):
        try:
            file = open(self.filename, 'r')
        except IOError:
            print "can't open file: %s" % self.filename 
        for e in file:
            e = e.rstrip("\n")
            if e != "":
                i = e.index('=')
                key = e[0:i]
                value = e[i+1:]
                if key == 'app_key':
                    self.app_key = value
                elif key == 'app_secret':
                    self.app_secret = value
                elif key == 'callback_url':
                    self.callback_url = value
                elif key == 'auth_code':
                    self.auth_code = value
                elif key == 'access_token':
                    self.access_token = value
                elif key == 'expires_in':
                    self.expires_in = value

    def printConf(self):
        print "AppKey:", self.app_key
        print "AppSecret:", self.app_secret
        print "CallbackUrl:", self.callback_url
        print "AuthCode:", self.auth_code
        print "AccessToken:", self.access_token
        print "ExpiresIn:", self.expires_in
        print "LastID:", self.last_id

    def saveConf(self):
        try:
            file = open(self.filename, 'w')
        except IOError:
            print "can't open file: %s for write" % filename

        file.write('app_key=' + self.app_key + os.linesep)
        file.write('app_secret=' + self.app_secret + os.linesep)
        file.write('callback_url=' + self.callback_url + os.linesep)
        file.write('auth_code=' + self.auth_code + os.linesep)
        file.write('access_token=' + self.access_token + os.linesep)
        file.write('expires_in=' + str(self.expires_in) + os.linesep)
        file.write('last_id=' + self.last_id + os.linesep)

        file.close()
            



    def main(self):
        self.readConf()
        self.printConf()

if __name__ == '__main__':
    c = WeiboConf("weibo_config")
    c.main()
    #c.printConf()

