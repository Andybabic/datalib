import csv
import json
import os
import random

from numpy import append, not_equal

class DatasetManager:
    """ This class processes all data in different formats.
    It serves to read, filter and save the data.
    All datas are working with a list of dictionaries.
    """
    
    file=None
    directorypath=None
    dictionary=None
    data=None
    
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
    
    def __init__(self,file ,logger ):

        self.file=file
        self.log= logger
        self.inflog= logger.InfoLogger(logger,__name__)
        self.errorlog= logger.ErrorLogger(logger,__name__)
        self.warnlog= logger.WarningLogger(logger,__name__)
        self.debug= logger.DebugLogger(logger,__name__)
        self.data = self.load()
        #self.checkData()  
          
          
          
    def load(self):
        if self.file.endswith('json'):
            print("json is loaded")
            return self.openJsonToArray()
        elif self.file.endswith('csv'):
            print("csv is loaded")
            return self.openCSVandLoadToArrayofDicts()
        elif self.file.endswith('tsv'):
            print("tsv is loaded")
            return self.openTSVandLoadToArrayofDicts()
        else:
            print("Data Type is unsupported")
            return None
            
        
#-----------------------------------------------------------------------------------------------------------------------        
    #function to open fomats and load to array of dictionaries
    def openCSVandLoadToArrayofDicts(self):
        """ open a csv and retrun a list of dictionaries """
        with open(self.file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            self.dictionary= list(reader)
            return list(reader)

    def openJsonToArray(self):
        """ open a json and retrun a list of dictionaries """
        data = self.importFile(self.file)
        data = json.loads(data)
        self.dictionary=data
        return data
    
    def openTSVandLoadToArrayofDicts(self):
        """ open a tsv and retrun a list of dictionaries """
        import csv
        data = []
        with open(self.file, 'r') as f:
                reader = csv.DictReader(f, delimiter='\t')
                
                
                for row in reader:
                    data.append(row)
        self.dictionary=data
        return data
    
    def importFile(self,filename):
        """ easy import of a file. """
        with open(filename, 'r') as f:
            return f.read()
    
    
#-----------------------------------------------------------------------------------------------------------------------
#Dictionary functions   
    
    
    def checkData(self):
        """ This function checks if the strukture of the data is correct."""
        heads=[]
        errordata=[]
        for key in self.dictionary[0]:
            heads.append(key)
        for row in self.dictionary:
            if len(row) != len(heads):
                errordata.append(row)
        return errordata
           
                    
    def removeEntries(self,list_of_dict, list_to_remove):
        """ This function removes the entries in the list_to_remove from the list_of_dict. """
        for d in list_to_remove:
            if d in list_of_dict:
                list_of_dict.remove(d)
        return list_of_dict
       

        
    def show(self,list=None):
        """ return the keys of the dataset """
        if list is not None:
            data=list
        else:
            data=self.dictionary
        print(str(len(data))+' Rows are loaded' )
        print()
        for key in data[0]:
            print(key)
            
    def getSample(self,list=None):
        """ This function returns a random sample of the dataset. """
        if list is not None:
            data=list
        else:
            data=self.dictionary
        return data[random.randint(0,len(data))]


    def getClasses(self,className,list=None):
        """ This function returns all variations of classes in the dataset """
        if list is not None:
            data=list
        else:
            data=self.dictionary
        classes = []
        for row in data:
            if row[className] not in classes:
                classes.append(row[className])
        return classes
        
        
    def getrandomint(self,min,max):
        return random.randint(min,max)

    def getRows(self,column,value=None):
        """ This function returns all rows that have the same value in the column. Is calue None so all columns are returned. """
        filtered = []
        for row in self.dictionary:
            if row[column] == value or value == None:
                filtered.append(row)
        return filtered
    

    
    def getValue(self,key,list = None):
        """ This function returns the value of the key in the list. Nice to handle IDs.
        if list is None, the function returns the value of the key in the dataset. 
        
        
        for example:
        list= {'id': '1', 'CounterSpeech': False, 'commentText': 'text....'},{'id': '2', 'CounterSpeech': True, 'commentText': 'text....'},....
        
        getValue('CounterSpeech',list)
        returns: [False, True]
        
        """
        results=[]
        if list == None:
            list = self.dictionary
        for row in list:
            try :
                results.append(row[key])
            except:
                print("Key not found")
                break
            
        return results
        
        
    def get(self):
        """ rturns the dataset """
        return self.dictionary
    
    
     

    #-----------------------------------------------------------------------------------------------------------------------
    #Save Data in  tsv
  

    def saveArrayOfDictionariesAsTSV(self, dictionaryList, filename,path=None, customhead= None):
        """ This function saves a list of dictionaries as a tsv file. """
        header = []
        for key in dictionaryList[0][0]:
            header.append(key)
            print(key)
        if path is not None:
            filename= os.path.join(path,filename)
        fieldhead=header
        if customhead is not None:
            fieldhead=customhead
        with open(filename, 'w') as output_file:
            dw = csv.DictWriter(output_file,  delimiter='\t', fieldnames= fieldhead)
            dw.writeheader()
            
            for row in dictionaryList:
                for data in row:
                    for i in header:
                        output_file.write( str(data[i]).replace('\n','').replace('\r','').replace('\t','') + '')
                        
                        
                        if i != header[-1]:
                            output_file.write('\t')
                output_file.write("\n")
                #dw.writerows(row)
                


    #-----------------------------------------------------------------------------------------------------------------------

    def removeFile(self,filename):
        """ This function removes a file. """
        if os.path.exists(filename):
            os.remove(filename)
            
    def removeDuplicates(self,data):
        """ This function removes duplicates from a list of dictionaries. """
        uniqueID = []
        unique = []
        for row in data:
            if row not in uniqueID:
                uniqueID.append(row)
                unique.append(row)
        return unique

    def search_for_id_in_list_of_dict(self,searchid, list_of_dict):
        """ This function searches for a id in a list of dictionaries. """
        for d in list_of_dict:
            if d['id'] == searchid:
                return d
        return None

    def removeNone(self,list_of_dict):
        """ This function removes Entries with None from a list of dictionaries and returns the new list. """
        for d in list_of_dict:
            if d is None:
                list_of_dict.remove(d)
        return list_of_dict

    def search_for_id_in_list_of_dict(self,searchID, list_of_dict):
        """" This function searches for a id in a list of dictionaries. """
        for d in list_of_dict:
            if d['id'] == searchID :
                return d
        return None


       
    #return a list of dictionaries with only the selected dictionary keys
    def reduce (self,list_of_Dict ,select):
        """ This function returns a list of dictionaries with only the selected dictionary keys. """
        reduced = []
        #look in a single row
        for row in list_of_Dict:
            reduceRow={} 
            for s in select:
                #print(row[s])
                reduceRow[s]=row[s]
            reduced.append([ reduceRow  ])
            
        return reduced
    

        
        
    def getKey(self,dictionary, value):
        """ This function returns the key of a value in a dictionary. """
        for key, val in dictionary.items():
            return key 
        
    def add(slef,dictionarylist,key,value):
        """ This function adds a value to a dictionary. """
        #dictionary[key]=value
        #return dictionary
        for dictionary in dictionarylist:
            
            dictionary[0][key]=value
            
        return dictionarylist
    
    def merge(self,datasets=[]):
        mergedlist=[]
        for d in datasets:
            for row in d:
                mergedlist.append(row)
        return mergedlist
    
    
    