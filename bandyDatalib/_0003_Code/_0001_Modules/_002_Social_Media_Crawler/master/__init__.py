import os   
import time   
import sys



from .submodul.crawlerTwitter import TweetCrawl as twitter
from .submodul.crawlerYoutube import YoutubeCrawl as youtube




class Modul:
    
    
    def __init__(self,mainModul):

        #init Logging from mainModul _0003_Code._0001_Modules._001_Main.master 
        logging= mainModul.log
        self.log= logging
        self.log_inf=    logging.InfoLogger(self.log,__name__)
        self.log_error=  logging.ErrorLogger(self.log,__name__)
        self.log_warnlog=logging.WarningLogger(self.log,__name__)
        self.log_debug=  logging.DebugLogger(self.log,__name__)
        self.runtime = mainModul.getruntime()
        self.settings= mainModul.getSettings()
        
        

        
    
    #--------------------------------------------Crawler -----------------
    def createTwitterCrawler(self, consumer_key=None,consumer_key_secret=None,access_token=None,access_token_secret=None):
        """ create and return a new twitter crawler, more information in the Submodule/CrawlerTwitter Module `submodul.crawlerTwitter`
        
        return array of json
        """
        if self.noneExist([ consumer_key,consumer_key_secret,access_token,access_token_secret]):
            if self.noneExist( [ 
                               self.settings.get("twitter_consumer_key"),
                               self.settings.get("twitter_consumer_key_secret"),
                               self.settings.get("twitter_access_token"),
                               self.settings.get("twitter_access_token_secret")
                               ] ):
                print("No Twitter settings found")
                return None
            else:
                consumer_key=self.settings.get("twitter_consumer_key")
                consumer_key_secret=self.settings.get("twitter_consumer_key_secret")
                access_token=self.settings.get("twitter_access_token")
                access_token_secret=self.settings.get("twitter_access_token_secret")
                
        """ create and return a new twitter crawler, more information in the CrawlerTwitter Module """
        twittersettings={"twitter_consumer_key":consumer_key, "twitter_consumer_key_secret":consumer_key_secret, "twitter_access_token":access_token, "twitter_access_token_secret":access_token_secret }
        self.settings.write({'Twitter':twittersettings})
        crawler = twitter(consumer_key,consumer_key_secret,access_token,access_token_secret,self.log,self.runtime)
        return crawler
    
    def createYoutubeCrawler(self,key=None):
        """ create and return a new youtube crawler, more information in the Submodule/CrawlerYoutube Module `submodul.crawlerYoutube`
        
        return array of json
        """
        if self.noneExist([key]):
            if self.noneExist([ self.settings.get("youtube_key")]):
                print("No Youtube credentials found")
                return None
            else:
                key=self.settings.get("youtube_key")  
        """ create and return a new youtube crawler, more information in the CrawlerYoutube Module """
        self.settings.write({"youtube_key":key})
        print("Youtube Key:",key)
        crawler = youtube( key,self.path ,self.log,self.runtime) 
        
        return crawler
    #--------------------------------------------End- Crawler -----------------

    def noneExist(self,list):
        """ check if a list contains None """
        for item in list:
            if item == None:
                return True
        return False