
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
    log_debug=None
    """" I can't programm without bugs, but the debug log helps me to find bugs """
    
     
    # initialize the class with the root directory of the dataset 
    def __init__(self,DEVELOPER_KEY,path,logger):
        self.path=path
        self.DEVELOPER_KEY = DEVELOPER_KEY
        self.youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, developerKey = self.DEVELOPER_KEY)
        
        self.log= logger
        self.inflog= logger.InfoLogger(logger,__name__)
        self.errorlog= logger.ErrorLogger(logger,__name__)
        self.warnlog= logger.WarningLogger(logger,__name__)
        self.debug= logger.DebugLogger(logger,__name__)
        
        
    def delay(self,t):
        """ Sometime the api is not so fast so we have to wait a little bit, on default it is 1.5 sec"""
        self.apiDelay=t
    
    

    def crawlList(self,list_id):
        """ This function crawl the data of a list of youtube id and return a list of dict"""
        results=[]
        counter = 0   
        error_counter = 0
        for toDO in tqdm(list_id):
            counter= counter+1
            if True:
                try:
                    request = self.youtube.commentThreads().list(
                        part="snippet",
                        id=toDO
                    )
                    response = request.execute()
                    results.append(response['items'])      
                    #time.sleep(self.apiDelay)     
                except:    
                    error_counter = error_counter + 1
                    continue
            pass
        self.errorlog.write("error_counter: ",error_counter)
        return self.listJsonToDict(results)
    
  
    
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
                
   
   
            
        
    