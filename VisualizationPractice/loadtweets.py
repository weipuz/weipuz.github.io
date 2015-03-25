from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2832187939-ATv9XfdOFKU3NoQScnjxpTAGcwkBnouAN6jIMqJ"
access_token_secret = "c3fdNVanofyNCBZxoRHk2b8vTSwDq4ET3RNQ0829jcD0U"
consumer_key = "SC5pkBDv2ExnzC1vDuseiKbJ8"
consumer_secret = "EbXaH7DIwZUlY9GJpf12hSCTV2oEFG2R53dn2zGQsQqNJtweaT"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: '#vote5sos','#votealall','#vote1duk','#votedebbyryan'
    stream.filter(track=['#vote5sos','#votealall','#vote1duk','#votedebbyryan'])
    