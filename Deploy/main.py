# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 09:46:44 2022

@author: marquinho
"""

import streamlit as st
import WebAppForCustomerSegmentation as WebApp
import About

#create the menu
st.sidebar.title('Menu')
Page_user = st.sidebar.selectbox(

'Choice',['Prediction for Customer Segmentation','About the author'] 
 
)

#change the pages
if Page_user == 'Prediction for Customer Segmentation':
    WebApp.code()
    
if Page_user == 'About the author':
    About.info()