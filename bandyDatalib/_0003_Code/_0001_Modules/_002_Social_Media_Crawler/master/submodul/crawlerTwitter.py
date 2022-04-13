
import tweepy
import time
from tqdm import tqdm
import json


class TweetCrawl:
      
    consumer_key = '3IQgyFFgzEVkp0JM13q5Oyhz2'
    consumer_key_secret = 'tZHpEGrrCNyNWcUuu6CLAneaXIs0bB8yMC05PSFjcTcPw29JB2'
    access_token = '1048593584495230976-d3jUPWXLAFlJXxw8TYAFVnPvUwVBSQ'
    access_token_secret = 'KVNckfJagv9ZUZylVhZL8O3OgM8t3nbtgUyBMmYi7YXY9'    
    tweetDelay=1.5  
    api=None
    

    
    file_name='.TwitterCrawledList.txt'
    
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
    def __init__(self,consumer_key,consumer_key_secret,access_token,access_token_secret, logging,runtime):
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
        
        
        self.run= runtime(__name__)
        
        
        
    #--------------------------------------------Start external Function ---------------------------------------------------------------------------    
        
    def delay(self,t):
        """" Set the delay between the tweets 
        default = 1.5 seconds"""
        self.tweetDelay=t
    
    
    # took a list of TweetId and return a list of crawled data tweets
    def crawlList(self,list_id,use_preload_only=None):    
        """" Crawls a list of tweet ID and returned it as list of objects,
        
        use_preload_only= True --> to use the preload data
        use_preload_only= False --> crawl hole list
        use_preload_only= None --> check if the data is already in the preload data and if not crawl it"""
        
        
        results=[]
        counter = 0   
        error_counter = 0
        for toDO in tqdm(list_id):
                
                #check if the tweet is already crawled in .runtime
                if self.run.search(toDO) and (use_preload_only is None or use_preload_only==True):
                    results.append(self.run.get)
                    
                else:
                    if use_preload_only==True:
                        continue
                    try:
                        tweetFetched = self.api.get_status(toDO)
                        tweet = tweetFetched._json
                        results.append(tweet)     
                        time.sleep(self.tweetDelay) 
                        self.run.add(toDO,tweet) 
                        counter= counter+1
                        
                    except:    
                        error_counter = error_counter + 1
                        continue
                pass
        

        
        self.log_warnlog.write().info("crawlList ("+str(len(list_id))+" - entries): Rusults="+str(len(results))+" ____"+str(counter)+" tweets crawled online --- "+str(error_counter)+" errors")
        self.run.done()
        return results
    
    def crawlUser(self,user_id):
            """" Crawls a user and returned it as a object"""
            try:
                tweetFetched = self.api.get_status(user_id)
                tweet = tweetFetched._json
                return self.listJsonToDict(tweet)
            except:    
                self.warnlog.write("error "+str(user_id) +" not found")
    
    
 