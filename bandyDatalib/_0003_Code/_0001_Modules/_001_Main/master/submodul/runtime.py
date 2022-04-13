
import numpy
import json
import os

class Runtime:
    """ This Script handle the Runtime and Store and handle Projects Runtime for better performance """

      
    get= None
    existDataID= set([])
    existData= {}

    
    file_name=None
    folder_name='.runtime'
    path=None
    
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
    
     
    # We need to save the data in a file, so we can load it in a later Run to reduce time for already finnished taks
    def __init__(self,own_name,logging = None):
        self.name= own_name
        
        self.createRuntime()
        
        
    
    #create a runtimeFolder if not exist
    def createRuntime(self):
        """ create a runtime folder if not exist """
        #self.path= os.path.join(self.folder_name)
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)   
        self.path= os.path.join(self.folder_name,self.name)
        self.openexistData(self.path)
        self.openexistDataID(self.path)
        
        
        
        
        
    # this function stores a list as a set 
    def add(self,id,data):
        self.existData[id]=data
        self.existDataID.add(id)

    # this function search for a data in the set and return the index of the data if it is in the set
    def search(self,data):
        if data in self.existDataID:
            self.get= self.existData[ data ] 
            return True
        else:
            return False
        
    def done(self):
        self.saveFile( self.existDataID,self.path+'IDs')
        self.saveFile( self.existData,self.path+'Data' )
    
    # this function sava the sed in a txt file in the runtime folder
    def saveFile(self,data,name):
        with open(name, 'w') as fobj:
            try:
                fobj.write(json.dumps(data))
            except:
                for x in data:
                    fobj.write(str(x) + "\n")
            #self.log_inf.write().info("Runtime Data is saved")
            
       






    # this function load the data from the runtime folder if not exist create a new one
    def openexistDataID(self,name):
        file =name+'IDs'
        if os.path.exists(file):
            with open(file) as file:
                lines = file.readlines()
                lines = [line.rstrip() for line in lines]
                for i in lines:
                    self.existDataID.add(i)
        else:
            #create empty txt file
            with open(os.path.join(file), 'w') as f:
                json.dump({}, f)
            
            
    def openexistData(self,name):
        file =name+'Data'
        if os.path.exists(file):
            with open(file) as f:
                self.existData = json.load(f)      
        else:
            #create empty txt file
            with open(os.path.join(file), 'w') as f:
                json.dump({}, f)
            
