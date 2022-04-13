import logging
import os




    

   
class Logger:
    """
    Use this snipped to log a message!
    
    class SampleClass:
    
        log=None
        log_inf=None
        log_error=None
        log_warnlog=None
        log_debug=None

     
        def __init__(self,logger,X,X,X):
            self.log= logger
            self.inflog= logger.InfoLogger(logger,__name__)
            self.errorlog= logger.ErrorLogger(logger,__name__)
            self.warnlog= logger.WarningLogger(logger,__name__)
            self.debug= logger.DebugLogger(logger,__name__)
        
        
    ------------------ Sample WriteLog ------------------
        self.log_inf.write('info')
        self.log_error.write('error')
        self.log_warnlog.write('warnlog')
        self.log_debug.write('debug')
    """        
     
    warningFile = None
    infoFile = None
    debugFile = None
    errorFile = None
    
    loggers = {}
    """Store all Loggers ini for later use"""   
    
    
    def __init__(self, path):
        self.path = path
        self.warningFile = self.path +'/warnings.log'
        self.infoFile = self.path +'/info.log'
        self.debugFile = self.path +'/debug.log'
        self.errorFile = self.path +'/errors.log' 
        
        
        self.iniLogFile(self.warningFile)
        self.iniLogFile(self.infoFile)
        self.iniLogFile(self.debugFile)
        self.iniLogFile(self.errorFile)
        
       
        
    def checkFileExists(self,path):
        return os.path.exists(path)

    def createTXTFile(self,path):
        with open(path, 'w') as f:
            f.close()
            
    def iniLogFile(self,path):
        if( not self.checkFileExists(path) ):
            self.createTXTFile(path)
       


    def setup_logger(self,logger_name, log_file, info=False, level=logging.INFO):
        global loggers
        
        if self.loggers.get(logger_name):
            return self.loggers.get(logger_name)
        else:
            l = logging.getLogger(logger_name)
            formatter = logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s','%m-%d %H:%M:%S')
            fileHandler = logging.FileHandler(log_file)
            fileHandler.setFormatter(formatter)
            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(formatter)
            #Write to a second file simultaneously
            if info == True:
                fileHandlerInfo = logging.FileHandler(self.infoFile)
                fileHandlerInfo.setFormatter(formatter)
                l.addHandler(fileHandlerInfo)
            l.setLevel(level)
            l.addHandler(fileHandler)
            l.addHandler(streamHandler)       
            self.loggers[logger_name] = l
            return l
        
        
        
        


 



#------------------ Different Logging Classes  -------------------------------------------------------------------------------------------------------

    class InfoLogger():
        l=None
        
        
        
        def __init__(self,master, name):
            master.setup_logger('info', master.infoFile)
            self.l = logging.getLogger('info')
            
            
        
        def write(self,): 
            return self.l
        
        
            
             
    


    class DebugLogger():
        l=None
        
        def __init__(self,master,name ):
            master.setup_logger('debug', master.debugFile,info=True)
            self.l = logging.getLogger('debug')
            
            #self.infoLogger = master.InfoLogger(master,name)

        def write(self,): 
            return self.l
                
                
                

    

    class WarningLogger:
        l=None
        
        def __init__(self,master, name):
            master.setup_logger('warnings', master.warningFile,info=True)
            self.l = logging.getLogger('warnings')
  
        def write(self,): 
            return self.l
                
               
            
            
    class ErrorLogger:
        l=None
        
        def __init__(self,master, name):
            master.setup_logger('errors', master.errorFile,info=True)
            self.l = logging.getLogger('errors')  
            

        def write(self,): 
            return self.l
                


    
