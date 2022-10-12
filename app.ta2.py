# -*- coding: utf-8 -*-
"""
Created by Bryse
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('RandomFR2.pkl', 'rb'))


# creating a function for Prediction

def Fraud_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'No Fraud detected'
    else:
      return 'Fraud detected'
  
    
  
def main():
    
    
    # giving a title
    st.title('Fraud Prediction Web App')
    
    
    # getting the input data from the user
    
    
    creditLimit = st.text_input('Credit Limit value')
    availableMoney = st.text_input('Available Money value')
    transactionAmount = st.text_input('Transaction amount value')
    posConditionCode = st.text_input('Pos Condition Code value')
    posEntryMode = st.text_input('Pos Entry Mode value')
    cardLast4Digits = st.text_input('Card Last Four Digits value')
    currentBalance = st.text_input('Current Balance value')
    cardCVV = st.text_input('Card Cvv value')
    enteredCVV = st.text_input('Entered Cvv value')
    
    
    
    
    # code for Prediction
    Transaction = ''
    
    # creating a button for Prediction
    
    if st.button('Fraud Test Result'):
        Transaction = Fraud_prediction([creditLimit, availableMoney, transactionAmount, posConditionCode, cardLast4Digits, currentBalance, cardCVV, enteredCVV, posEntryMode])
        
        
    st.success(Transaction)
    
    
    
    
    
if __name__ == '__main__':
    main()