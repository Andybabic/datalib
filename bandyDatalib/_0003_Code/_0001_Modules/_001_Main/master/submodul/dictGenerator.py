import os


class DictGenerator:
      
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
        #self.path = os.path.abspath(os.path.join(path, os.pardir))
        if exist==None:
            self.project_path=self.createproject()
        else:
            self.project_path=self.setProject(exist)
        
        self.log= logger
        self.inflog= logger.InfoLogger(logger,__name__)
        self.errorlog= logger.ErrorLogger(logger,__name__)
        self.warnlog= logger.WarningLogger(logger,__name__)
        self.debug= logger.DebugLogger(logger,__name__)
        

   



    def createproject(self):
        name= self.path
        print('Creating project: '+name)
        if not os.path.exists(os.path.join(name,'001_original_data')):
            
            os.makedirs(  os.path.join(name,'001_original_data'))    
            os.makedirs(  os.path.join(name,'002_intermediate_data'))
            os.makedirs(  os.path.join(name,'003_clean_dataset'))  
            self.creat_empty_MD_file( os.path.join(name))
            print('Project created: '+name)
            
        else:
            print('Error, Project already exist')
        
        self.original_data_path= os.path.join(name,'001_original_data')
        self.itermediate_data_path= os.path.join(name,'002_intermediate_data')
        self.clean_dataset_path= os.path.join(name,'003_clean_dataset')
        self.project_path=name
        return self.project_path
            


    def setProject(self,project):
        if os.path.exists(project):
            try:
                self.project_path=project
                self.original_data_path= os.path.join(project,'001_original_data')
                self.itermediate_data_path= os.path.join(project,'002_intermediate_data')
                self.clean_dataset_path= os.path.join(project,'003_clean_dataset')
                print('Project set: '+project)
                return self.project_path
            except:
                print('Error, Project not found')
                self.log_error.write('Error, Project not found')
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
    

    def get_original_data_path(self):
        return self.original_data_path
    
