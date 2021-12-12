import logging
import os







    

   
class BandyLogger:
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

    def __init__(self, path):
        self.path = path
        self.warningFile = path +'/warnings.log'
        self.infoFile = path +'/info.log'
        self.debugFile = path +'/debug.log'
        self.errorFile = path +'/errors.log' 
        self.iniLogFile(self.warningFile)
        self.iniLogFile(self.infoFile)
        self.iniLogFile(self.debugFile)
        self.iniLogFile(self.errorFile)
        
       
        
    def checkFileExists(self,path):
        return os.path.exists(self.path)

    def createTXTFile(self,path):
        with open(path, 'w') as f:
            f.write()
            f.close()
            
    def iniLogFile(self,path):
        if( not self.checkFileExists(path)):
            self.createTXTFile(path)
    

    class InfoLogger():
        def __init__(self,master, name):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.INFO)
            infoFormatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
            file_handler = logging.FileHandler(master.infoFile)
            file_handler.setFormatter(infoFormatter)
            self.logger.addHandler(file_handler)
        

        def write(self, msg):
            self.logger.info(msg)
            


    class DebugLogger():
        
        
        def __init__(self,master,name ):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.DEBUG)
            debugFormatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
            file_handler = logging.FileHandler(master.debugFile)
            file_handler.setFormatter(debugFormatter)
            self.logger.addHandler(logging.StreamHandler())
            self.infoLogger = master.InfoLogger(master,name)
        
        

        def write(self, msg):
            self.logger.debug(msg)
            self.infoLogger.write(msg)

    

    class WarningLogger:
        def __init__(self,master, name):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.WARNING)
            warningFormatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
            file_handler = logging.FileHandler( master.warningFile)
            file_handler.setFormatter(warningFormatter)
            self.logger.addHandler(file_handler)
            self.infoLogger = master.InfoLogger(master,name)
        

        def write(self, msg):
            self.logger.warning(msg)
            self.infoLogger.write(msg)
            
            
    class ErrorLogger:
        def __init__(self,master, name):
            self.logger = logging.getLogger(name)
            self.logger.setLevel(logging.ERROR)
            errorFormatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
            file_handler = logging.FileHandler(master.errorFile)
            file_handler.setFormatter(errorFormatter)
            self.logger.addHandler(file_handler)
            self.infoLogger = master.InfoLogger(master,name)
        

        def write(self, msg):
            self.logger.error(msg)
            self.infoLogger.write(msg)