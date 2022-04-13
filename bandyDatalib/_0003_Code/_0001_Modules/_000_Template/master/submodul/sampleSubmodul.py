

import time
from tqdm import tqdm



class SampleSubmodul:
    
    # initialize the class with the root directory of the dataset 
    def __init__(self,logging):
       
        self.log= logging
        self.log_inf=logging.InfoLogger(logging,__name__)
        self.log_error=logging.ErrorLogger(logging,__name__)
        self.log_warnlog=logging.WarningLogger(logging,__name__)
        self.log_debug=logging.DebugLogger(logging,__name__)
    
        
    def sampleFunc(self):
        
        self.log_inf.info("ich bin ein sample Log von sampleSubmodul")
        return ( "Hallo Welt")