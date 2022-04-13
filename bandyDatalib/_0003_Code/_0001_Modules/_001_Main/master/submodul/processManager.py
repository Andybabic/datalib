
import multiprocessing

from multiprocessing import Process, Queue


class ProcessManager:

    log=None
    log_inf=None
    log_error=None
    log_warnlog=None
    log_debug=None
    task=None
    process=None
    Q = Queue()
    running= True
   

     
    # initialize the class 
    def __init__(self, logger,task ):
        self.task=task
        self.log= logger
        self.inflog= logger.InfoLogger(logger,__name__)
        self.errorlog= logger.ErrorLogger(logger,__name__)
        self.warnlog= logger.WarningLogger(logger,__name__)
        self.debug= logger.DebugLogger(logger,__name__)
        print('ProcessManager initialized')
        
        
        
        
        
        
    def customfunction(self,x):
        """ create your own function """
        #self.log_inf("this Text is a log_inf")
        return x
    

        
    def process_start(self):
        self.process = Process(target=self.task.run_task())
        self.process.start()
        
        
    
    
    #this function retrun the status of the process
    def isRunning(self):
        return self.process.is_alive()
    
    def wait(self):
        while self.process.is_alive():
            pass

        


