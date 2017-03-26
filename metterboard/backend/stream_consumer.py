from tweepy import API, StreamListener, OAuthHandler, Stream, TweepError
from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

class MBStreamListener(StreamListener):
    """Custom implemented of tweepy StreamListener class"""
    
    def on_status(self, status):
        print status
        self.store_status(status)

    def store_status(self, status):
        import pdb; pdb.set_trace()
        

if __name__ == '__main__':
    import pdb; pdb.set_trace()
    print CONSUMER_KEY
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = API(auth)

    mb_stream_listener = MBStreamListener()
    mb_stream = Stream(auth=api.auth, listener=mb_stream_listener)
    mb_stream.filter(track=['dick'])
