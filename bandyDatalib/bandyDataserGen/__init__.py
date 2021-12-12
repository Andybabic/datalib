       
import os   
import json   
       
from . import crawlerTwitter as twitter
from . import crawlerYoutube as youtube
from . import datasetManager as datasetM
from . import bandyDictGenerator as dictGen
from . import bandylogger as logger



class Master:
    """
        The master class initializes the entire infrastructure based on a path.
        It needs a path (in which the project is located) and an optional project folder. If no project folder is specified, a new one is created.
        Afterwards the entire folder structure is either read or created.   
        
        Sample usage: 
        
        def getcurrentpath():
            return os.path.dirname(os.path.abspath(__file__))
            
        test=Module.Master(getcurrentpath(),exist='001_Dataset') 

    """
    
    settings= None
    """ handle the Json file with the settings """
    project= None
    """ handle the Project Class"""
    project_path= None
    """ simple String with the absolute Path to the project """
    
    
    
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
    

  
    
    
    
    def __init__(self,path,exist=None):
        self.path = path
        self.project= dictGen.BandyDictGenerator(path, None, exist)
        logging= logger.BandyLogger(self.project.project_path)
        self.log= logging
        self.log_inf=logging.InfoLogger(logging,__name__)
        self.log_error=logging.ErrorLogger(logging,__name__)
        self.log_warnlog=logging.WarningLogger(logging,__name__)
        self.log_debug=logging.DebugLogger(logging,__name__)
        self.project= dictGen.BandyDictGenerator(path, logging, exist)
        self.project_path= self.project.project_path
        self.jsonpath = self.project_path+"/settings.json"
        self.settings= self.checkSetting()
        
        
        
    
    
    def createSetting(self):
        """ crate a new setting file """
        with open(self.jsonpath, 'w') as f:
            json.dump({}, f)
        return self.readFromSetting()
    
    
    def writeDictSetting(self,data):
        """ write to the setting file """
        with open(self.jsonpath, 'w') as f:
            json.dump(data, f)
        return self.readFromSetting()
            
    
    def readFromSetting(self):
        """ load the settings from the setting file """
        with open(self.jsonpath, 'r') as f:
            data = json.load(f)
        return data
    
    def checkSetting(self):
        """ look if the setting file exists, if not create a new one """
        if os.path.exists(self.jsonpath):
            return self.readFromSetting()
        else:
            return self.createSetting()
    
    

    def createTwitterCrawler(self, consumer_key,consumer_key_secret,access_token,access_token_secret):
        """ create and return a new twitter crawler, more information in the CrawlerTwitter Module """
        crawler = twitter.TweetCrawl(consumer_key,consumer_key_secret,access_token,access_token_secret,self.log)
        return crawler
    
    def createYoutubeCrawler(self,key):
        """ create and return a new youtube crawler, more information in the CrawlerYoutube Module """
        crawler = youtube( key, self.log)
        return crawler

        
    def setDataset(self,key):
        """ create and return a new youtube crawler, more information in the CrawlerYoutube Module """
        crawler = youtube( key, self.log)
        return crawler