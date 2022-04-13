



class STR_Filter:
  
  
    
    log=None
    log_inf=None
    log_error=None
    log_warnlog=None
    log_debug=None

     
    # initialize the class 
    def __init__(self , logger):
        
        self.log= logger
        self.inflog= logger.InfoLogger(logger,__name__)
        self.errorlog= logger.ErrorLogger(logger,__name__)
        self.warnlog= logger.WarningLogger(logger,__name__)
        self.debug= logger.DebugLogger(logger,__name__)


    def remove_at(self,data):
        """ ake a list of data and remove all chars between "@" and first ' ' from Strings """
            char_list=[]
            char_count= 0
            
            string_text= data['text']
            for i in string_text:   
                if len(char_list) >= 1:
                    if i  == ' ':
                        string_text= string_text.replace(list2string(char_list),' ')
                        char_list=[]
                    else :
                        char_list.append(i)
                if i == '@':
                    char_list.append(i)
            data['text']= string_text
            return data

    
    def remove_hashtags(self,data):
        """ ake a list of data and remove all chars between "@" and first ' ' from Strings """
            char_list=[]

            char_list=[]
            char_count= 0
            
            string_text= data['text']
            for i in string_text:   
                if len(char_list) >= 1:
                    if i  == ' ':
                        string_text= string_text.replace(list2string(char_list),' ')
                        char_list=[]
                    else :
                        char_list.append(i)
                if i == '@':
                    char_list.append(i)
            data['text']= string_text
            return data

    def all(self,data_As_List,func):
        for listitem in data_As_List:
            if type(listitem) == type(list()):
                Searchall(listitem,func)
            else: 
                data[0]=func(data[0])
                
    def list2string(self,list):
        string=''
        for i in list:
            string+=i
        return string           
            
        

        
    