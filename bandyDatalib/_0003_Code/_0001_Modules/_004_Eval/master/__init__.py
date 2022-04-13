from sklearn.metrics import classification_report
import time   
import shutil
import os,sys,inspect


current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))


class Modul:
    
    
    def __init__(self,master):
        self.master= master

        #init Logging from mainModul _0003_Code._0001_Modules._001_Main.master 
        logging= master.log
        self.log= logging
        self.log_inf=    logging.InfoLogger(self.log,__name__)
        self.log_error=  logging.ErrorLogger(self.log,__name__)
        self.log_warnlog=logging.WarningLogger(self.log,__name__)
        self.log_debug=  logging.DebugLogger(self.log,__name__)
        self.runtime = master.getruntime()
        self.settings= master.getSettings()
        
        

        
    def pathbuilder(self,list_of_direcories):
        """ build a path from a list of directories """
        #check if last element contains a dot or underline

        path=""
        for direc in list_of_direcories:
                path=os.path.join(path, direc)
            
            
        if not os.path.exists(path):
            print("file dont exists")
            print("path: "+path)
            return self.createfolder(path)
            
        else: return path


       
    def createfolder(self,name):
        
        """ create a new folder in the Dataset project """
        if not os.path.exists(name):
            os.makedirs(name)
        return os.path.join(name)
    
    def move_folder(self,source,dest):
        import shutil
        """ move a folder to a new location """
        if not os.path.exists(dest):
            os.makedirs(dest)
        print("moving folder: "+source+" to: "+dest)
        self.rename_folder (shutil.move(source,dest))
        
    # rename folder
    def rename_folder(self,old_name):
        """ rename a folder """
        new_name= old_name.replace(".","")
        if not os.path.exists(new_name):
            os.rename(old_name,new_name)
        else:
            print("folder already exists")

    def copy_element(self,source,dest):
        """ copy a file or folder to a new location """
        if not os.path.exists(dest):
            os.makedirs(dest)
        shutil.copy(source,dest)
  

        
    def close(self,notebook):
        dateString = time.strftime("%Y%m%d_%H_%M_")
        """ move the temp folder to the eval folder """
        eval_runs_folder=self.pathbuilder([root,'_0004_Evaluation','_002_Runs',dateString+self.settings.get("project_name")])
        self.settings.write(  { "eval_runs_folder":  eval_runs_folder })
        self.copy_element(notebook, self.settings.get("eval_runs_folder"))
        self.copy_element(self.settings.get("settings_path"),self.settings.get("eval_runs_folder"))
        self.move_folder(self.settings.get("output_dir"), self.settings.get("eval_runs_folder"))
        
        


        
    #save classification_report to file as csv
    def save_classification_report(self,report):
        """ save the classification report to a file """
        report_path=self.settings.get("output_dir")  
        report_path=os.path.join(report_path,"classification_report.csv")
        with open(report_path, 'w') as f:
            f.write(report)
        return report_path

    def getResults(self):
        print(self.master.defaultSeed)
        """ get the results from the model """
        #print(classification_report(self.master.model_results[0], self.master.model_results[1]))
        #test
        return self.save_classification_report(classification_report(self.master.model_results['y_true'], self.master.model_results['y_pred']))
