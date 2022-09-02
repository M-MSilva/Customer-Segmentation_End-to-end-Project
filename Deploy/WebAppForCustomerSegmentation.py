# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 08:27:45 2022

@author: marquinho
"""

import pickle 
import pandas as pd
import streamlit as st
from pathlib import Path
import os


def header():
    
    #we found where the file trained_model.sav is
    current_directory = Path(__file__).parent #Get current directory
    file = open(os.path.join(current_directory, 'trained_model.sav'), 'rb') #rb = read bytes because we are reading the file
     
    #read the trained_model.sav file
    loaded_model = pickle.load(file)
    
    # Web App Title
    st.write("""
    ## Prediction for Customer Segmentation app
    
    #### Developed by: Marcos Matheus de Paiva Silva
    
    This is a web application built and hosted on Streamlit, whose purpose is to segment customers. In this project we deal with a **clustering** problem.
    
    **Links:** My [Linkedin](https://www.linkedin.com/in/marcos-matheus-silva-089699b3/) , [GitHub](https://github.com/M-MSilva) and [email](silvamarcosxd@gmail.com).
    """)
    
    
    return loaded_model



def Predict_Points(input_data,loaded_model):
    
    #predict
    prediction = loaded_model.predict(input_data)

    
    #show the result
    if(prediction == 0):
     st.markdown(''' #### You are part of group 1:
                    ''')
     st.write("""In this group the quantity of goods ordered is about 27.5, the price of each good purchased is approximately 100 dollars.
                 In addition, total purchases are approximately 3000 dollars, the largest purchases occur in December and the most consumed 
                 product line is classic cars, and the agreements with these individuals are medium to small.""")
    else:
        if(prediction == 1):
         st.markdown(''' #### You are part of group 2:
                        ''')
         st.write("""
                     In this group, the quantity of goods ordered is about 45, purchases more products in the range of 100 dollars, 
                     as well as having total purchases of about 4000 dollars. Their purchases occur more frequently in December and the most consumed product line is classic cars.
                     The agreements with this group are medium-sized""")
        else:
            st.markdown(''' #### You are part of group 3:
                        ''')
            st.write("""
                     In this group, the amount of merchandise ordered is about 30, buys more products in the range of 65 dollars, 
                     as well as having total purchases of about 1600 dollars. This group buys more in December and the most purchased 
                     product line is vintage cars. Agreements with this group are small.
                     """)
    
    
def code():	   

    #collect the model read
    loaded_model = header()    

    #fill out form
    form = st.form(key='dados')    
    QUANTITYORDERED	= form.number_input('Generally how many product orders does the customer place?',key='1', min_value=0,value=45,step=1)
    PRICEEACH = form.number_input('what is the approximate price of each product that the customer buys?',value=100,key='2')
    STATUS = form.selectbox("Generally what is the status of the customer's order?",['Shipped','Cancelled','Resolved','On Hold','In Process','Disputed'],key='3')
    MONTH_ID = form.number_input('In which month was the order placed?', key='4', min_value=0, max_value=12,value=12,step=1)
    PRODUCTLINE = form.selectbox("The product line that the customer usually buys is ?",['Classic Cars','Vintage Cars','Motorcycles','Planes','Trucks and Buses','Ships','Trains'],key='5')
    MSRP = form.number_input("Does the user know the manufacturer's suggested retail price?",value=100,key=6)
    COUNTRY	 = form.selectbox("What country is the customer from? If you don't have yours here, put the closest one.",['USA','Spain','France',
                                                                                                                       'Australia','UK','Italy',
                                                                                                                 'Finland','Norway','Singapore',
                                                                                                                       'Canada','Denmark','Germany',
                                                                                                                       'Sweden','Austria','Japan'
                                                                                                                       ,'Belgium','Switzerland','Philippines',
                                                                                                                       'Ireland'],key=7)
    DEALSIZE = form.selectbox("How big is the deal?",['Medium','Small','Large'],key=8)
    form.form_submit_button('Add')
    
    #calculate total sales value
    SALES = QUANTITYORDERED*PRICEEACH
       
   
    #dataset creation
    data = [[QUANTITYORDERED,PRICEEACH,SALES,STATUS,MONTH_ID,PRODUCTLINE,MSRP,COUNTRY,DEALSIZE]]
    columns = ['QUANTITYORDERED','PRICEEACH','SALES','STATUS','MONTH_ID','PRODUCTLINE','MSRP','COUNTRY','DEALSIZE']
    
    
    #insert
    df = pd.DataFrame(data=data, columns=columns)
    
    
    #creating a button for prediction
    if st.button('Result'):
        Predict_Points(df,loaded_model)
    
    

if __name__ == '__main__':
    code()		
