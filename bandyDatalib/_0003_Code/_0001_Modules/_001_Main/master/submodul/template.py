



class Template:
  
    teplatevariable= None
    
    log=None
    log_inf=None
    log_error=None
    log_warnlog=None
    log_debug=None

     
    # initialize the class 
    def __init__(self, teplatevariable , logger):
        self.pateplatevariableth=teplatevariable
        
        self.log= logger
        self.inflog= logger.InfoLogger(logger,__name__)
        self.errorlog= logger.ErrorLogger(logger,__name__)
        self.warnlog= logger.WarningLogger(logger,__name__)
        self.debug= logger.DebugLogger(logger,__name__)
        
        
        
    def customfunction(self,x):
        """ create your own function """
        self.log_inf("this Text is a log_inf")
        return x
    
    

            
        
    