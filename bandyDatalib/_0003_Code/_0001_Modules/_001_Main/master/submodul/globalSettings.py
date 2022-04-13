import os   
import json     
import sys
import random
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import random_seed




class GlobalSettings:
  
    path= None
    
    log=None
    log_inf=None
    log_error=None
    log_warnlog=None
    log_debug=None

     
    # initialize the class 
    def __init__(self, path , logger):
        self.path=path
        
        
        self.log= logger
        self.log_inf= logger.InfoLogger(logger,__name__)
        self.errorlog= logger.ErrorLogger(logger,__name__)
        self.warnlog= logger.WarningLogger(logger,__name__)
        self.debug= logger.DebugLogger(logger,__name__)
        
        
        self.jsonpath = os.path.join(path, "settings.json")
        self.settings= self.checkSettingfile()
        
        print("init MasterModule done")
        self.write({"project_path":path})
        self.write({"settings_path":self.jsonpath})
        self.write ({"project_name":path.split('/')[-1]})
        
#-------------------------------------------- Start External Function ---------------------------------------------------------------------------   
        
    def write(self,list):
        """ write to the setting file, create a new one if it does not exist """
        
    
        if len(list)>0:
            for key in list:
                self.settings[key]=list[key]
                self.save()       
                self.log_inf.write().info( "Updated Settings: " + str(key+" : "+str(list[key])) )
        else:
            self.save()
            
    def get(self,key):
        self.reloadsettings()
        """ get the setting from the settings.json file 
        
        Return Value:  INT, FLOAT, STRING, BOOL
        None if the key is not found
        
        """
        if key in self.settings:
            return self.settings[key]
        else:
            print( "Value of " + str(key) +" not found in settings")
            return None
        

 #-------------------------------------------- End External Function ---------------------------------------------------------------------------

 #-------------------------------------------- Start-Internal Helper---------------------------------------------------------------------------
    
    def createSetting(self):
        """ crate a new setting file """
        with open(self.jsonpath, 'w') as f:
            json.dump({}, f)
        return self.openFile()
    
    def save(self):
        """ save the settings to the settings.json file """
        with open(self.jsonpath, 'w') as f:
            json.dump(self.settings, f, sort_keys=True,indent=4, separators=(',', ': '))
    

    def openFile(self):
        """ load the settings from the setting file """
        with open(self.jsonpath, 'r') as f:
            data = json.load(f)
        return data
    
    def random_seed(self,seed=356):
        """ Sets all seed to the seed provided as parameter,
        additinally the TF_DETERMINISTIC_OPS is set to
        True in order to obtain reproducible results
        with the GPU.
        """
        random.seed(seed)
        os.environ['PYTHONHASHSEED'] = str(seed) # Python general
        np.random.seed(seed)
        tf.random.set_seed(seed)
        tf.keras.seed = seed
        os.environ['TF_DETERMINISTIC_OPS'] = '1'
        self.write({"random_seed":seed})
        self.log_inf.write().info("Set random seed to " + str(seed))
        self.defaultSeed=seed
        return random.random()
    
    
    

    
    def updateSettings(self,key,value):
        valueOld=self.setting.get(key)
        """ update the settings.json file """
        self.reloadsettings()
        #self.log_inf.write("Updated Settings" + str(key+" : "+value)+ "---OLD : " + str(valueOld))
    
    def checkSettingfile(self):
        """ look if the setting file exists, if not create a new one """
        if os.path.exists(self.jsonpath):
            return self.openFile()
        else:
            return self.createSetting()
        
    def reloadsettings(self):
        """ reload the settings from the setting file """
        self.settings= self.checkSettingfile()
        
        

    
    
    def setSeed(self,seed):
        """ set the random seed """
        self.randomseed=seed
        self.setting.set({"random_seed":seed})
        self.log_inf.write().info("Set random seed to " + str(seed))
    
    
