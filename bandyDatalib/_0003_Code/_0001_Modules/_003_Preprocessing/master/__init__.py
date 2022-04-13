import os   
import time   
import sys




from .submodul.filter_strings import STR_Filter as str_filter




class preprocessing:
    
    
    def __init__(self,masterModul):

        #init Logging from masterModul _0003_Code._0001_Modules._001_Main.master 
        logging= masterModul.log
        self.log= logging
        self.log_inf=    logging.InfoLogger(self.log,__name__)
        self.log_error=  logging.ErrorLogger(self.log,__name__)
        self.log_warnlog=logging.WarningLogger(self.log,__name__)
        self.log_debug=  logging.DebugLogger(self.log,__name__)
        
        
        self.project= dictGen(path, self.log, exist)
        """ handle the Project Class """
        self.settings = gs(self.path,self.log)
        self.ini_settings()
        
    
    def get_filter(self,)
        return str_filter( self.log)