


    

def get(self,model_Name):
    
    create_csv(self)
    if model_Name == '_0001_Model_Bert':
        from .._0002_Models import _0001_Model_Bert as main_bert
        #Need: self,master,seed,logging,runtime
        model=main_bert.Bert(master=self,logging=self.log,runtime=self.getruntime)
        #create and return a Runtimeprocess for the model
        run= returnprocess(self,model)
        #run= model
        return  run
    
    
    
    if model_Name == '_0002_Model_T5':
        from .._0002_Models import _0001_Model_Bertalt as main_bert
        #Need: self,master,seed,logging,runtime
        return main_bert.Bert(master=self ,logging=self.log,runtime=self.getruntime)

    if model_Name == '_0003_Model_Bert_Multi':
        from .._0002_Models import _0003_Model_Bert_Multi as main_bert
        #Need: self,master,seed,logging,runtime
        model=main_bert.Bert(master=self,logging=self.log,runtime=self.getruntime)
        #create and return a Runtimeprocess for the model
        run= returnprocess(self,model)
        #run= model
        return  run
    
    else:
        print('Model not found')

#convert the model in a runtime process
def returnprocess(self,model):
        run= self.make_process(model)
        return run
        
        

#create infratructure for the model
def create_csv(self):
    import csv
    import os
    self.settings.write(  { "result_data": os.path.join(   self.settings.get("output_dir")   ,"results.csv",) })
    filename=  self.settings.get("result_data")
    print(filename)

    #create a csv file
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Model', 'Run', 'Epoch', 'Loss', 'Accuracy', 'Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()