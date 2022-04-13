
import googleapiclient.discovery
import time
from tqdm import tqdm
import argparse
import youtube_dl



class YoutubeCrawl:
    """ This class is used to crawl the youtube data ( infos and videos)
    yout can read the documentation of the youtube api on https://github.com/ytdl-org/youtube-dl
    
    All Viedeos the crawler will download will be in the 002_intermediate/youtubeDownloads folder
    """
      
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = None
    youtube=None
    path=None
     
    apiDelay=1.5  
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
    log_log_debug=None
    """" I can't programm without bugs, but the log_debug log helps me to find bugs """
    
     
    # initialize the class with the root directory of the dataset 
    def __init__(self,DEVELOPER_KEY,path,logging, runtime):
        self.path=path
        self.DEVELOPER_KEY = DEVELOPER_KEY
        self.youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, developerKey = self.DEVELOPER_KEY)
        
        self.log= logging
        self.log_inf=logging.InfoLogger(logging,__name__)
        self.log_error=logging.ErrorLogger(logging,__name__)
        self.log_warnlog=logging.WarningLogger(logging,__name__)
        self.log_debug=logging.DebugLogger(logging,__name__)
        
        self.run= runtime(__name__)    
        
        
    def delay(self,t):
        """ Sometime the api is not so fast so we have to wait a little bit, on default it is 1.5 sec"""
        self.apiDelay=t
    
    
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
                            request = self.youtube.commentThreads().list(
                                part="snippet",
                                id=toDO
                            )
                            response = request.execute()
                            results.append(response['items'])
                            self.run.add(toDO,response['items']) 
                            
                        except:    
                            error_counter = error_counter + 1
                            continue
                    pass
            
            self.log_warnlog.write().info("crawlList ("+str(len(list_id))+" - entries): Rusults="+str(len(results))+" ____"+str(counter)+" tweets crawled online --- "+str(error_counter)+" errors")
            self.run.done()
            return results
    
    def getData(self,contentid):
        """ This function return the data of a single youtube id"""
        request = self.youtube.commentThreads().list(
            part="snippet",
            id=contentid
        )
        response = request.execute()
        return self.listJsonToDict(response['items'])


    def listJsonToDict(self,list_json):
        """ This function convert a list of json to a list of dict"""
        list_dict=[]
        for json in list_json:
            list_dict.append(json)
        return list_dict
    
    def videodownloader(self,videoId,path):
        """ This function download the video of a youtube video id in the intermediate folder"""
        url = 'https://www.youtube.com/watch?v='+videoId
        ydl_opts = {
            'format': 'bestvideo/best',
            'outtmpl': path+'/youtubeDownloads/' +videoId+'_' +'%(title)s.%(ext)s',
            'noplaylist': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
                
   
   
            
        
    