#   importing dependencies
import os
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import pandas as pd

from ppf.config.configuration import ConfigurationManager
from ppf.entity import ModelEvaluationConfig
from ppf.logging import logger


# loading configuration manager
config = ConfigurationManager()
config = config.get_model_evaluation_config()


st.title('Petrol Price Forecasting')

if 'count' not in st.session_state:
    st.session_state.count = 0


def main():
    def callback_search():
    #   Destroying old sessions
        st.session_state['search_btn'] = False


    #   Range for the future months
    list = [i for i in range(1, 16)]
    st.write('Future data for next 15 months')
    option = st.selectbox(
        'decide how many future months you want to predict into?',
        list,
        on_change=callback_search
    )


    #   loading model
    model = pickle.load(open(config.model_path, 'rb'))
    logger.info('Model loaded successfully')

    # loading datasets
    train_dataset = pd.read_csv(config.train_data_path, index_col=False) 

    # setting 'Date' as an index column and changing its datatype to Datetime
    train_dataset.set_index('Date', inplace=True)
    train_dataset.index = pd.to_datetime(train_dataset.index)
    train_dataset.columns = ['Past price']


    prediction = st.button('Predict')
    # adding session state fot 'prediction' button
    if st.session_state.get('search_btn') != True:
        st.session_state['search_btn'] = prediction

    # prediction and printing the output
    if st.session_state['search_btn']:
        predictions = model.predict(len(train_dataset), len(train_dataset)+option-1)
        df_predicted = pd.DataFrame(predictions)
        df_predicted = df_predicted.rename(columns={'predicted_mean': 'Forecasted Price'})
        
        st.write('Predictions') 
        st.write(df_predicted)
        

        # ploting the predictions
        fig, ax = plt.subplots()
        train_dataset.plot(ax=ax, legend=True, label='Past Price')
        predictions.plot(ax=ax, legend=True, label='Forecasted Price')
        ax.set_title('forecasted plot')
        ax.set_ylabel('Price (USD)')
        st.pyplot(fig)

if __name__ == '__main__':

    if (st.session_state.count == 0):
        st.session_state.count += 1
        os.system("python main.py")
        logger.info("Training Successful!")
        
    main()
        




    
