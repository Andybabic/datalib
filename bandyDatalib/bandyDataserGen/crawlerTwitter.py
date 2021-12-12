
import tweepy
import time
from tqdm import tqdm

class TweetCrawl:
      
    consumer_key = ''
    consumer_key_secret = ''
    access_token = ''
    access_token_secret = ''     
    tweetDelay=1.5  
    api=None
    
    log=None
    """ log is a class that handles the logging of the master class, 
    it is a class that is used to log the information, warnings and errors.
    this class is passed to all modules 
    """
    log_inf=None
    """ every step of the project should be saved, so every log ist saved in the info.log file """
    log_error=None
    """ only for crash error handling """
    log_warnlog=None
    """ sometimes it the code will work, but the data are not correct but the code will pass. User this log for warnings """
    log_debug=None
    """" I can't programm without bugs, but the debug log helps me to find bugs """
    
     
    # initialize the class with the root directory of the dataset 
    def __init__(self,consumer_key,consumer_key_secret,access_token,access_token_secret, logging):
        self.consumer_key = consumer_key
        self.consumer_key_secret = consumer_key_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)  
        
        self.log= logging
        self.log_inf=logging.InfoLogger(logging,__name__)
        self.log_error=logging.ErrorLogger(logging,__name__)
        self.log_warnlog=logging.WarningLogger(logging,__name__)
        self.log_debug=logging.DebugLogger(logging,__name__)
        
        
        
        
        
    def delay(self,t):
        self.tweetDelay=t
    
    
    # took a list of TweetId and return a list of crawled data tweets
    def crawlList(self,list_id):
        results=[]
        counter = 0   
        error_counter = 0
        for toDO in tqdm(list_id):
            counter= counter+1
            if True:
                try:
                    tweetFetched = self.api.get_status(toDO)
                    tweet = tweetFetched._json
                    results.append(tweet)      
                    time.sleep(self.tweetDelay)     
                except:    
                    error_counter = error_counter + 1
                    continue
            pass
        self.warnlog.write("error_counter: ",error_counter)
        return self.listJsonToDict(results)
    
    def crawlUser(self,user_id):
            try:
                tweetFetched = self.api.get_status(user_id)
                tweet = tweetFetched._json
                return self.listJsonToDict(tweet)
            except:    
                self.warnlog.write("error "+str(user_id) +" not found")
    
    
    #this function convert a list of json in a list of dict
    def listJsonToDict(self,list_json):
        list_dict=[]
        for json in list_json:
            list_dict.append(json)
        return list_dict
    
    
 