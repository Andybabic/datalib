
import random


class Datasplitter:
    
  
    dataframe= None
    seed=None
    test=None
    val=None
    train=None
    
    log=None
    log_inf=None
    log_error=None
    log_warnlog=None
    log_debug=None

  
    # initialize the class  
    def __init__(self, dataframe, seed ,logging ,train_in_percent ,test_in_percent):
        self.dataframe=dataframe
        self.seed=seed
     
        
        self.log= logging
        self.log_inf=logging.InfoLogger(logging,__name__)
        self.log_error=logging.ErrorLogger(logging,__name__)
        self.log_warnlog=logging.WarningLogger(logging,__name__)
        self.log_debug=logging.DebugLogger(logging,__name__)
        print(len(dataframe))
        return self.split_data(train_in_percent, test_in_percent)
        
   
        
    # split the dataframe randomly ( seed ) into train and test data, rest is validation data
    def split_data(self, train_in_percent, test_in_percent):
        """ split the dataframe randomly ( seed ) into train and test data, rest is validation data
        return: train, test, val  - list of dataframes
        """
        self.log_inf.write().info("Start split dataframe")
        self.log_inf.write().info("Train percentage: " + str(train_in_percent))
        self.log_inf.write().info("Test percentage: " + str(test_in_percent))
        self.log_inf.write().info( "Seed: " + str(self.seed))
        random.seed( self.seed )
        random.shuffle( self.dataframe )
        train_size=int(len(self.dataframe)* train_in_percent)
        test_size=int(len(self.dataframe)*  test_in_percent)
        self.log_inf.write().info( "Train size: " + str(train_size))
        self.log_inf.write().info( "Test size: " + str(test_size))
        self.train=self.dataframe[:train_size]
        self.test=self.dataframe[train_size:train_size+test_size]
        self.val=self.dataframe[train_size+test_size:]
        self.log_inf.write().info( "Train size: " + str(len(self.train)))
        self.log_inf.write().info( "Test size: " + str(len(self.test)))
        self.log_inf.write().info("Validation size: " + str(len(self.val)))
        self.log_inf.write().info("End split dataframe")
        
    