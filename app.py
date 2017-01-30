# -*- coding: utf-8 -*-

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from json import loads, dumps
import unicodedata
#Variables that contains the user credentials to access Twitter API
access_token = "190915689-e5aDtxOEvIMEYBs1zKnX8swQzlcCfAAVhHsEq0ar"
access_token_secret = "Ej2ski37dgpBGXFakdcygjEwJZ4uog15ANq26kZ0kXLM5"
consumer_key = "fZVawApfuVx0mzzAUgYsfBJZW"
consumer_secret = "CbIsXZIkXsNmRX7OqYxWG8PGbONuJJhK0jexQhT3Zf1egbQO3q"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def strip_accents(self,s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                       if unicodedata.category(c) != 'Mn')

    def on_data(self, data):
        #dt = loads(data)
        dt = self.strip_accents(data).encode('ascii', 'ignore').decode('ascii')
        #print dt["retweeted_status"]["user"]["screen_name"], dt["created_at"]
        with open("TweetFile.json", 'a') as tf:
            tf.write(dt.replace('\n','')+',')
        #for i in data:
        #    print i
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    a = stream.filter(track=['@LassoGuillermo','@andrespaezec','@PacoMoncayo',
                             '@MonseBustamant','@daloes10','@ramiroaguilart',
                             '@Lenin', '@JorgeGlas', '@CynthiaViteri6',
                             '@MauricioPozoEC', '@pesanteztwof', '@a_alcivar',
                             '@IvanEspinelM','@ZuquilandaDuque']
                      #0.040131, -78.578703
                      #-0.375845, -78.292458
                      #locations=[0.04013112, -78.57870312, -0.37584512, -78.29245812]
                      )
