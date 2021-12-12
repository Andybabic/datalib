import os


class BandyDictGenerator:
      
    original_data_path = None
    itermediate_data_path = None
    clean_dataset_path = None
    project_path = None
     
     
     
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
    """
    initialize the class with the root directory of the dataset 
    """
    def __init__(self,path,logger=None,exist= None):
        self.path = path
        if exist==None:
            self.project_path=self.createproject()
        else:
            self.project_path=self.setProject(exist)
        if logger is None:
            self.log=None
            self.inflog=None
            self.errorlog=None
            self.warnlog=None
            self.debug=None
        else:   
            self.log= logger
            self.inflog= logger.InfoLogger(logger,__name__)
            self.errorlog= logger.ErrorLogger(logger,__name__)
            self.warnlog= logger.WarningLogger(logger,__name__)
            self.debug= logger.DebugLogger(logger,__name__)
        

    # Count the number of files in a directory and return the number rised by one
    def count(self):
        count = 0
        for file in os.listdir(self.path):
            if os.path.isdir(file) and not file.startswith("."):
                count = count+1
        
        return count



    def createproject(self):
        idname = self.count()+1
        name= str(self.getIDString(idname) +'_Dataset')
        if not os.path.exists(name):
            os.makedirs(name)
            
            os.makedirs(  os.path.join(name,'001_original_data'))
            self.original_data_path= os.path.join(name,'001_original_data')
            os.makedirs(  os.path.join(name,'002_intermediate_data'))
            self.itermediate_data_path= os.path.join(name,'002_intermediate_data')
            os.makedirs(  os.path.join(name,'003_clean_dataset'))
            self.clean_dataset_path= os.path.join(name,'003_clean_dataset')
            self.creat_empty_MD_file( os.path.join(name))
            self.project_path=name
            print('Project created: '+name)
            return self.project_path

        else:
            print('Error, Project already exist')
            


    def setProject(self,project):
        if os.path.exists(project):
            self.project_path=project
            self.original_data_path= os.path.join(project,'001_original_data')
            self.itermediate_data_path= os.path.join(project,'002_intermediate_data')
            self.clean_dataset_path= os.path.join(project,'003_clean_dataset')
            print('Project set: '+project)
            return self.project_path
        else :
            print('Error, Project not found')
            print('Error, '+project+' not found:')

    
    def getIDString(self,id):
        formatId = str(id+1000)
        return  formatId[1:]  
    
    
    
    
    def goIn(self,folder_path, folder):
        if os.path.exists(os.path.join(folder_path, folder)):
            return os.path.join(folder_path, folder)
        else:
            print('Error, directory not found') 
            
    def goOut(self,folder_path):
            return os.path.join(folder_path).parent
     

    
    def creat_empty_MD_file(self,projectpath):
        file_name = os.path.join(projectpath,'dataset.md')
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                f.write("hello World")
            return 'done'
        else:
            return 'The file already exist'
    

