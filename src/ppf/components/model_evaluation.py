import os
from ppf.logging import logger
from ppf.entity import ModelEvaluationConfig


from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import pickle



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self):
        #   loading model
        model = pickle.load(open(self.config.model_path, 'rb'))
        
        # loading datasets
        train_dataset = pd.read_csv(self.config.train_data_path, index_col=False)  
        test_dataset = pd.read_csv(self.config.test_data_path, index_col=False)  
        
        # setting 'Date' as an index column and changing its datatype to Datetime
        train_dataset.set_index('Date', inplace=True)
        train_dataset.index = pd.to_datetime(train_dataset.index)
        test_dataset.set_index('Date', inplace=True)
        test_dataset.index = pd.to_datetime(test_dataset.index)


        # predicting
        # predictions = model.predict(test_dataset)
        
        # print(predictions)
        predictions = model.predict(len(train_dataset), len(train_dataset)+15)
        df_predicted = pd.DataFrame(predictions)
        df_predicted.to_csv(self.config.predictions_path)
        
        # train_dataset.plot(legend=True, label='Train', figsize=(10,5))
        # predictions.plot(legend=True, label='Prediction')