#!/usr/bin/env python2.7
import os
class Conf(object):
    def __init__(self, filename):
        self.consumer_key=""
        self.consumer_secret=""
        self.access_token=""
        self.access_token_secret=""
        self.filename = filename
        self.last_id = ""
        self.readConf()
    def readConf(self):
        try:
            file = open(self.filename, 'r')
        except IOError:
            print "can't open file: %s" % filename 
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
                elif key == 'last_id':
                    self.last_id = value

    def printConf(self):
        print "ConsummerKey:", self.consumer_key
        print "ConsumerSecret:", self.consumer_secret
        print "AccessToken:", self.access_token
        print "AccessTokenSecret:", self.access_token_secret
        print "LastID:", self.last_id

    def saveConf(self):
        try:
            file = open(self.filename, 'w')
        except IOError:
            print "can't open file: %s for write" % filename

        file.write('consumer_key=' + self.consumer_key + os.linesep)
        file.write('consumer_secret=' + self.consumer_secret + os.linesep)
        file.write('access_token=' + self.access_token + os.linesep)
        file.write('access_token_secret=' + self.access_token_secret + os.linesep)
        file.write('last_id=' + self.last_id + os.linesep)
        file.close()
            



    def main(self):
        self.readConf()
        self.printConf()

if __name__ == '__main__':
    c = Conf("config")
    c.main()
    c.saveConf()

