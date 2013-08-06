#!/usr/bin/env python2.7
class Conf(object):
    def __init__(self, filename):
        self.consumer_key=""
        self.consumer_secret=""
        self.access_token=""
        self.access_token_secret=""
        self.filename = filename
        self.readConf()
    def readConf(self):
        try:
            file = open(self.filename, 'r')
        except IOError:
            print "can't open file: ", filename 
        x = 0
        for e in file:
            e = e.rstrip("\n")
            if e != "":
                i = e.index('=')
                key = e[0:i]
                value = e[i+1:]
                if key == 'consumer_key':
                    self.consumer_key = value
                elif key == 'consumer_secret':
                    self.consumer_secret = value
                elif key == 'access_token':
                    self.access_token = value
                elif key == 'access_token_secret':
                    self.access_token_secret = value

    def printConf(self):
        print "ConsummerKey:", self.consumer_key
        print "ConsumerSecret:", self.consumer_secret
        print "AccessToken:", self.access_token
        print "AccessTokenSecret:", self.access_token_secret


    def main(self):
        self.readConf()
        self.printConf()

if __name__ == '__main__':
    c = Conf("config")
    c.main();

