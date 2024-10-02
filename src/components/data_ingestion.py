# Take data as input and give Train and Test data as output
import os
import sys
# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from logger import logging
from exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## intialize the data ingestion configuration

@dataclass
class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')


## create a data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')

        try:
            csv_path=os.path.join('E:/Data Science materials/Machine Learning/DiamondPricePrediction_ML_Project/notebooks/Data','gemstone.csv')
            logging.info('Dataset read as pandas Dataframe')
            logging.info(f"Reading dataset from {csv_path}")

            df = pd.read_csv(csv_path)
            logging.info(f'Dataset successfully read with shape: {df.shape}')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train test split")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is completed')

            return (
                        self.ingestion_config.train_data_path,
                        self.ingestion_config.test_data_path
            )



        except Exception as e:
            logging.info('Error occured in Data Ingestion config')
# ## initialize the data ingestion configuration(all the parameter required for data ingestion class to store data path or the process of defining how data is stored and mapped to a new storage scheme)

# @dataclass
# class DataIngestionConfig:
#     train_data_path = os.path.join('artifacts','train.csv')
#     test_data_path = os.path.join('artifacts','test.csv')
#     raw_data_path = os.path.join('artifacts','raw.csv')
    
# ## create a data ingestion class (responsible for data read, train, test and split)

# class DataIngestion:
#     def __init__(self):
#         self.ingestion_config=DataIngestionConfig() #parameter of dataingestionconfig come into ingestion_config
    
#     ## below function will do read data, train,test and split and store
#     def initiate_data_ingestion(self):
#         logging.info("Data Ingestion Method Start")
        
#         # write try catch block in every file where main operation occurs. This is generic
#         try:
#             df = pd.read_csv(os.path.join("notebooks/Data",'gemstone.csv'))
#             logging.info("Dataset read as pandas DataFrame")
            
#             os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            
#             df.to_csv(self.ingestion_config.raw_data_path,index = False)
            
#             # train test split
#             logging.info("train test split")
#             train_set, test_set = train_test_split(df,test_size = 0.3, random_state = 40)
            
#             train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
#             test_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
#             logging.info("ingestion of data is completed")
            
#             return (self.initiate_data_ingestion.train_data_path, self.initiate_data_ingestion.test_data_path)
            
#         except Exception as e:
#             logging.info("Error occuered in data ingestion config")
