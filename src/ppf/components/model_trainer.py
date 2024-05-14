import os
from ppf.logging import logger
from ppf.entity import ModelTrainerConfig


from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import pickle


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
    
        dataset = pd.read_csv(self.config.data_path, index_col=False)  
        dataset.set_index('Date', inplace=True)
        dataset.index = pd.to_datetime(dataset.index)
        # print(dataset)

        model=ARIMA(dataset, order=(self.config.p, self.config.d, self.config.q))
        model_fit=model.fit()
        
        # save model
        pickle.dump(model, open(self.config.model_path, 'wb'))
        logger.info(f'Model is stored as {self.config.model_path}')