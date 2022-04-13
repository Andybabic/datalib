import os   
import time   
import sys
import shutil



from .submodul.datasetManager import DatasetManager as datasetM
from .submodul.dictGenerator import DictGenerator as dictGen
from .submodul.logger import Logger as logger
from .submodul.datasplitter import Datasplitter as datasplitter 
from .submodul.runtime import Runtime as runtime
from .submodul.processManager import ProcessManager as processManager
from .submodul.globalSettings import GlobalSettings as gs



import os,sys,inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

sys.path.insert(0, root)


#import Models
import _0003_Code._0002_Models  as model






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
    """ handle the Json file with the settings ( it will generate by the dictGen class) ), 
    for example settings.json"""
  
    defaultSeed= 356 
    """ can be chached later by function random_seed('int') """
    
 
    
    log=None
    """ log is a class that handles the logging of the master class, 
    it is a class that is used to log the information, warnings and errors.
    this class is passed to all modules 
    """
    log_inf=None
    """ every step of the project should be saved, so every log ist saved in the `submodul.logger` file """
    log_error=None
    """ only for crash error handling """
    log_warnlog=None
    """ sometimes it the code will work, but the data are not correct but the code will pass. User this log for warnings """
    log_debug=None
    """" I can't programm without bugs, but the debug log helps me to find bugs """
    model_results=None
    


    
    
    
    def __init__(self,path,exist=None):
        self.path = path 
        logging= logger(self.path)
        self.log= logging
        self.log_inf=    logging.InfoLogger(self.log,__name__)
        self.log_error=  logging.ErrorLogger(self.log,__name__)
        self.log_warnlog=logging.WarningLogger(self.log,__name__)
        self.log_debug=  logging.DebugLogger(self.log,__name__)
        
        
        self.project= dictGen(path, self.log, exist)
        """ handle the Project Class """
        self.settings = gs(self.path,self.log)
        self.ini_settings()
        
    
    
     #--------------------------------------------Set default Settings ---------------------------------------------------------------------------
    def ini_settings(self):
        
        # create a string in format of 20211112_19_04_
        
       
        self.settings.write(  { "output_dir":  self.pathbuilder([self.path,".output"]) })
        self.settings.write(  { "temp_folder":  self.pathbuilder([self.settings.get("output_dir")]) })
        self.settings.write(  { "result":       self.pathbuilder([self.settings.get("output_dir"),"results",]) })
       
     #--------------------------------------------Start-Extrernal Functions ---------------------------------------------------------------------------
     
    def getSettings(self):
        """ returns the settings class """
        return self.settings

     
    #-------------------------------------------- Start-Models --------------------------------------
    
    #get name of the last path element
    
        
        
    
    
    def getModels(self,model_Name):
        """ handle Models to the project
        More information in the Code/Models Module  `model` 
        
        model = master.getModels('_0001_Model_Bert')
        
        returns the model class 
        
        
        features: model.start()"""
        return model.get(self,model_Name)
    
    
    #-------------------------------------------- End-Models ---------------------------------------
    

     #--------------------------------------------Start-Init Modules ----------
    
    def make_process(self,task):
        """ Make a multithread process, 
        when it finished the task, it will kill the process automatically,
        no GPU blocking or other problems, the task.class needs to have a function called 'start'
        
        task= processManager( SortNumbers() )
        task.process_start()
        return: process"""
        return processManager(self.log,task)
 
    
    #--------------------------------------------Start- Data Handler -----------------    
    def setDataset(self,directorie,file):
        """ create and return a new datasetmanager, more information in the DatasetManager Module `submodul.datasetManager`"""
        path= self.pathbuilder( [directorie , file] )
        self.settings.write({"dataset_file":path})
        print(path)
        datset = datasetM(path,self.log)
        return datset
    

    
    def splitDataset(self,dataset ,train = None ,test = None):
        """ split the dataset test, train, val datasets 
        example:
        
        Data = splitDataset(dataset,train=0.7,test=0.2)
        Data.test --> extenss 70% of the dataset
        Data.train --> extenss 20% of the dataset
        Data.val --> extenss 10% of the dataset
        """
        if train == None or test == None:
            test= 0.2 if self.settings.get("test_size")==None else self.settings.get("test_size")
            train= 0.7 if self.settings.get("train_size")==None else self.settings.get("train_size")
        
        self.settings.write({ "datasplitter_train":train, "datasplitter_test":test})
        
        splitter= datasplitter(dataset,self.defaultSeed,self.log,train,test)
        return splitter
    
    #--------------------------------------------End- Data Handler ----------------- 
    #--------------------------------------------End-Init Modules ----------------------------------
    #--------------------------------------------End-Extrernal Functions -----------------------------------------
    
    
    
    
    #--------------------------------------------same internal helpers ---------------------------------------------------------------------------
    


    def getruntime(self):
        """ return the runtime of the program """
        return runtime
    
    def pathbuilder(self,list_of_direcories):
        """ build a path from a list of directories """
        #check if last element contains a dot or underline

        path=""
        for direc in list_of_direcories:
                path=os.path.join(path, direc)
            
            
        if not os.path.exists(path):
            print("file  is created")
            print("path: "+path)
            return self.createfolder(path)
            
        else: return path
    
        
    def createfolder(self,name):
        
        """ create a new folder in the Dataset project """
        if not os.path.exists(name):
            os.makedirs(name)
        return os.path.join(name)
    

     
        
    