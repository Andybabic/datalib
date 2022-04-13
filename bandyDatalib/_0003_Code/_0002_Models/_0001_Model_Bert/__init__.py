import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.models import Model
import tensorflow.keras.optimizers as tf_optimizers

from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import random
import sys
from sklearn.metrics import classification_report as clsr


class Bert:
    
    run=None
    done=False
   
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

        
    
    """" Use default settings for the model when no settings are given
    if there are no Settings in the settings file ( dataset folder ), the default settings are used and saved in the settings file """
    
    default_settings={
        "verbose": True,
        "TF_VERBOSE": 1,
        "NUM_CLASS":2,
        "GLOBAL_BATCH_SIZE": 9,
        "EPOCHS": 9,
        "LEARNING_RATE": 1e-5,
        "BETA_1": 0.9,
        "BETA_2": 0.999,
        "EPSILON": 1e-8,
        "MAX_SEQUENCE_LENGTH": 384,
        "optimizer_name": 'Adam',
      
        }
    
    

    settings=None
    
    
        
    def __init__(self,master,logging,runtime):
        """ initialize the class with the root directory of the dataset """
        self.log= logging
        self.log_inf=logging.InfoLogger(logging,__name__)
        self.log_error=logging.ErrorLogger(logging,__name__)
        self.log_warnlog=logging.WarningLogger(logging,__name__)
        self.log_debug=logging.DebugLogger(logging,__name__)
        self.master=master
        self.settings = master.settings
        
        self.results_data_csv= self.settings.get("result_data" )
        if self.settings.get("Bert_Settings" ) is None:
           self.model_settings= self.default_settings
        else:
            self.model_settings= self.settings.get("Bert_Settings" )
        self.settings.write({"Bert_Settings": self.model_settings } )    
        self.setSettings()
        self.set_struktur()
        self.log_inf.write().info("Bert successfully initialized")
  
    
    

        
        
        
        
        

             
        
        
        
        
    def create_text_model(vocab_size, max_len, embedding_dim, units, batch_size):
            model = tf.keras.Sequential([
                tf.keras.layers.Embedding(vocab_size, embedding_dim, batch_input_shape=[batch_size, max_len]),
                tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units)),
                tf.keras.layers.Dense(units, activation='relu'),
                tf.keras.layers.Dense(1, activation='sigmoid')
            ])
            return model
        
    def optimizer_builder(self,optimizer_name):
                classname =getattr(tf_optimizers, optimizer_name) 
                return classname
        
    def setSettings(self):
           
          
            #Verbose settings:
            self.verbose = self.model_settings['verbose']
            self.TF_VERBOSE = self.model_settings['TF_VERBOSE'] # 1 = Progress bar 2 = one line per epoch only!
            # Classes:
            self.NUM_CLASS = self.model_settings["NUM_CLASS"]  # Counterspeech | NO Counterspeech
            # Hyperparameters
            self.GLOBAL_BATCH_SIZE = self.model_settings["GLOBAL_BATCH_SIZE"]
            self.EPOCHS = self.model_settings["EPOCHS"]
            # Optimizer parameters:
            # Adam
            self.LEARNING_RATE = self.model_settings['LEARNING_RATE'] # Changed for finetuning
            self.BETA_1 = self.model_settings['BETA_1']
            self.BETA_2 = self.model_settings['BETA_2']
            self.EPSILON =   self.model_settings['EPSILON']
            #optimizers:
            
            # Bert Parameters
            self.MAX_SEQUENCE_LENGTH = self.model_settings['MAX_SEQUENCE_LENGTH']


            #build a optimizer
            customOpt = self.optimizer_builder(self.model_settings['optimizer_name'])
            self.optimizer = customOpt(learning_rate=self.LEARNING_RATE, beta_1=self.BETA_1, beta_2=self.BETA_2, epsilon=self.EPSILON )
            #self.optimizer = Adam(learning_rate=self.LEARNING_RATE, beta_1=self.BETA_1, beta_2=self.BETA_2, epsilon=self.EPSILON )
            
            
            

  
  

        
            
            
            self.log_inf.write().info("Set Settings")
            self.log_inf.write().info("Batch Size: "+str(self.GLOBAL_BATCH_SIZE))
            self.log_inf.write().info("Epochs: "+str(self.EPOCHS))
            self.log_inf.write().info("Optimizer: "+str(self.optimizer))
            self.log_inf.write().info("Learning Rate: "+str(self.LEARNING_RATE))
            self.log_inf.write().info("Beta_1: "+str(self.BETA_1))
            self.log_inf.write().info("Beta_2: "+str(self.BETA_2))
            self.log_inf.write().info("Epsilon: "+str(self.EPSILON))
            self.log_inf.write().info("BERT Max sequence length: "+str(self.MAX_SEQUENCE_LENGTH))
            self.log_inf.write().info("Set Settings successfully")
            
    def set_struktur(self):
        root = os.path.dirname(os.path.abspath(__file__))
     
        
        project_root = self.master.project.project_path
        self.output= self.master.createfolder(os.path.join(project_root,".output"))
        self.settings.write({"output_dir": self.output } ) 
        dataset_dir = self.master.project.clean_dataset_path
      
        
        self.bert_model_dir = os.path.join(root, 'BERT_Models', 'multi_cased_L-12_H-768_A-12')
        self.pathToBertVocabFile = os.path.join(self.bert_model_dir, "vocab.txt")
        self.bert_ckpt_file = os.path.join(self.bert_model_dir, "bert_model.ckpt")
        self.bert_config_file = os.path.join(self.bert_model_dir, "bert_config.json")

      
        self.data_dir = dataset_dir

        self.train_tsv = os.path.join(self.data_dir, "train.tsv")
        self.val_tsv = os.path.join(self.data_dir, "val.tsv")
        self.test_tsv = os.path.join(self.data_dir, "test.tsv")

        self.checkpointDir = os.path.join(self.output, "checkpoints")
        



        
                

    def run_task(self):
        from bert.tokenization.bert_tokenization import FullTokenizer
  
       
        from time import time, gmtime, strftime
        from bert.tokenization.bert_tokenization import FullTokenizer

        from .final_models import create_text_model

        from .my_utils.callbacks.MyCallbacks import MyCallbacks
        from .my_utils.textUtils.textpreprocessing import EXISTDataTrainVal,EXISTDataTestwithLabels
        from .my_utils.modelUtils.modelUtils import calcAccTextModel
        from .my_utils.callbacks.callbackUtils import plotTimesPerEpoch
        from .my_utils.fileDirUtils.fileDirUtils import createDirIfNotExists

        import seaborn as sn

        from sklearn.metrics import accuracy_score
        from sklearn.metrics import f1_score
        from sklearn.metrics import confusion_matrix

        import warnings

        
     
        self.current_time = datetime.now().strftime("%Y-%m-%d_%H_%M")
        #Checkpoint settings:
        self.checkpoint_name = f'bert_only_{self.MAX_SEQUENCE_LENGTH}'
        self.checkpointDir = os.path.join(self.checkpointDir, (self.checkpoint_name + '_' + self.current_time))
        
        fileName="weights-improvement-{epoch:02d}-{val_accuracy:.2f}.hdf5"
        filePath = os.path.join(self.checkpointDir, fileName)
        df_train = pd.read_csv(self.train_tsv, header=0, sep='\t')
        df_val = pd.read_csv(self.val_tsv, header=0, sep='\t')
        df_test = pd.read_csv(self.test_tsv, header=0, sep='\t')


        
        
        df_train.Class.count()
        df_train_true = len(df_train.loc[(df_train.Class == 1)])
        df_train_false = len(df_train.loc[(df_train.Class == 0)])
        df_total = len(df_train)

        bigger_class = None
        if df_train_false >= df_train_true:
            bigger_class = df_train_false
        else:
            bigger_class = df_train_true
            
        baseline = round((bigger_class * 100)/df_total)

        if (baseline >= 60):
            self.log_error.write().error("Bert-----> Warning: Baseline is greater than threshold")

        self.log_inf.write().info("The zero baseline for this set is: " + str(baseline) + "%. ")
        
        tokenizer = FullTokenizer(vocab_file=self.pathToBertVocabFile)
        text_data_train = EXISTDataTrainVal(df_train, df_val, tokenizer, [0,1], self.MAX_SEQUENCE_LENGTH, 'Text', 'Class')
        
        tensorboardDir = os.path.join(self.checkpointDir, 'tensorboard')

        createDirIfNotExists(tensorboardDir )
        createDirIfNotExists(self.checkpointDir )

        callbacks_list = MyCallbacks(tensorboardDir, filePath, earlyStopping=True).createCheckpoints()

        self.log_inf.write().info("Starting with Text Model, checkpoints can be found in " + str(self.checkpointDir))
        
        
        
        
        
        
        #-----------------------------------------
        
        
        start = time()
            
        model = create_text_model(self.MAX_SEQUENCE_LENGTH, self.bert_ckpt_file, self.bert_config_file, self.NUM_CLASS, isPreTrained=False) 

        if self.verbose:
            model.summary()
            
                    
        model.compile(  loss=keras.losses.SparseCategoricalCrossentropy(),
            optimizer=self.optimizer,
            metrics=['accuracy'])
            
    

        if self.verbose:
            model.summary()
            for layer in model.layers:
                    print(layer.name, layer.trainable)           
                    
                    
        history = model.fit(
            text_data_train.train_x, text_data_train.train_y,
            validation_data = (text_data_train.val_x, text_data_train.val_y),
            callbacks=callbacks_list,
            batch_size=self.GLOBAL_BATCH_SIZE,
            epochs=self.EPOCHS,
            verbose = self.TF_VERBOSE
        )

        end = time()
        timeProceed = (end - start) / 60
        print(f'It took {timeProceed} minutes to train everything' )
        plotTimesPerEpoch(callbacks_list)
        
        text_data_test = EXISTDataTestwithLabels(df_test, tokenizer, [0,1], self.MAX_SEQUENCE_LENGTH, 'Text', 'Class')
        data  = calcAccTextModel(model, text_data_test.test_x, text_data_test.test_y, 'Val', self.GLOBAL_BATCH_SIZE)
        y_true = data[0]
        test_max = data[1]
        y_pred = pd.Series(test_max, name = 'Predicted')
        y_true = pd.Series(y_true, name = 'Val Y') 
        
        
        df_confusion = pd.crosstab(y_true, y_pred, margins=True)
        
        plt.figure(figsize = (10,7))
        sn.heatmap(df_confusion, annot=True, fmt='g')
        
        def plot_confusion_matrix(y, y_pred, labels):
            ax= plt.subplot()
            cm = confusion_matrix(y, y_pred)
            sn.heatmap(cm, annot=True, ax=ax, fmt='g') #annot=True to annotate cells

            ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels')
            ax.set_title('Confusion Matrix'); 
            ax.xaxis.set_ticklabels(labels, rotation=45)
            ax.yaxis.set_ticklabels(labels, rotation=45)
            plt.show()
        print("Nr. 11")
        plot_confusion_matrix(y_true, y_pred, ['Class False', 'Class True'])
        
        print (f' F1 Score is = {f1_score(y_true, y_pred)}')
        
        import csv
        from datetime import date
        today = date.today()

        def createAndJoin(dic):
                if not os.path.exists(dic):
                    #check if dic is a file of type csv
                    if not os.path.isfile(dic):
                        os.makedirs(dic)
                    else:
                        with open(os.path.join(dic), 'w', newline='') as csvfile:
                            csvfile.close()
                return dic
       
        results_data_dir = createAndJoin(os.path.join(self.output, "bert"))
        
      
                
  
            
            
        

        results=[]


        with open(self.results_data_csv, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                results.append(row)
                print(row)


        CUSTOM_TEXT = f'Batch Size: {self.GLOBAL_BATCH_SIZE}, Epochs: {self.EPOCHS}, Optimizer: Adam, Learning Rate; {self.LEARNING_RATE}, Beta_1: {self.BETA_1}, Beta_2: {self.BETA_2}, Epsilon: {self.EPSILON}, BERT Max sequence length: {self.MAX_SEQUENCE_LENGTH}'


        new_row={'Date': self.current_time,'Batch Size': self.GLOBAL_BATCH_SIZE, 'Epochs': self.EPOCHS, 'Learning Rate;': self.LEARNING_RATE, 'Time': timeProceed, 'Score': f1_score(y_true, y_pred), 'Accuracy': 'none','Loss': 'none'}
        last_row= {}

        with open(self.results_data_csv, 'w') as csvfile:
            fieldnames = ['Date','Dataset','Comment','Batch Size', 'Epochs','Learning Rate;', 'Time','Score', 'Accuracy','Loss',]
            
        
                
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            

            writer.writeheader()
            for row in results:
                writer.writerow(row)
                last_row= row
                
            if last_row == new_row:
                print('keine neuen Daten vorhanden')
            else:
                print('neuen Daten vorhanden')
                writer.writerow(new_row)


        print('ist working!!!!!!!!!')
      
        print("Bert is done")
        self.done=True
  

        self.send_to_master({'y_true': y_true, 'y_pred': y_pred, 'f1_score': f1_score(y_true, y_pred), 'accuracy': 'none', 'loss': 'none'}) 
        
        


    def send_to_master(self,list_data):
        self.master.model_results= list_data