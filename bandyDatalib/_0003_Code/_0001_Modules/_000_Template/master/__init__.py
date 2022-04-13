import os   
import time   
import sys



from .submodul.sample import Sample as sampleSubmodul





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
        
        

        
  
    def sampleFunc(self):
        """ check if a list contains None """
        self.log_inf.info("ich bin ein sample Log")
        self.settings.write({'sample':'Hallo Welt})'})
        return ( self.settings.get({'sample':'Hallo Welt})'}))

    def getSample(self):
        
        return sampleSubmodul(self.log)