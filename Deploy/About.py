# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:12:16 2022

@author: marquinho
"""

import streamlit as st


def info():
    st.write("""
    ## About the author
    
    My name is **Marcos Matheus** and I have a degree in **computational physics** from Federal Fluminense University. I'm a developer
    methodical, persistent and dedicated. Of the languages, frameworks and related I work with include:
    
    """)
    
    images = ["https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-plain-wordmark.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-plain-wordmark.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-plain.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-plain.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/laravel/laravel-plain-wordmark.svg",
    "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-plain-wordmark.svg"]
    
    
    
    st.image(images, width=40)
    
    st.write("""
    This project is part of my personal portfolio which is available on [GitHub](https://github.com/M-MSilva), this program uses **clustering** techniques, but in my portfolio I have several other **regression** and **classification** projects.

    In addition to being graduated in computational physics, I have the following courses:
        
    * Advanced SQL (by Kaggle);
    * Applied Machine Learning in Python (by Coursera - Michigan University);
    * Data Visualization With Python (by Federal University of Lavras);
    """)
