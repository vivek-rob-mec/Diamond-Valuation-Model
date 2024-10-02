import os
import sys
import pandas as pd
# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from logger import logging
from exception import CustomException
from components.data_ingestion import DataIngestion
from components.data_transformation import DataTransformation
from components.model_trainer import ModelTrainer

## to trigger DataIngestion
if __name__ =='__main__':
    # obj = DataIngestion() ## will return path of data stored i.e train_data,test_data,raw_data
    # train_data_path,test_data_path=obj.initiate_data_ingestion()
    obj=DataIngestion()
    train_data_path, test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
    
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation_obj(train_data_path,test_data_path)
    
    model_trainer = ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)