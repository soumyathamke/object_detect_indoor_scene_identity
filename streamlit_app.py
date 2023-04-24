
import streamlit as st
import numpy as np

from  PIL import Image, ImageEnhance


#Create two columns with different width
col1, col2 = st.columns( [0.8, 0.2])
with col1:               # To display the header text using css style
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload your photo here...</p>', unsafe_allow_html=True)
    

  
#Add a header and expander in side bar
st.sidebar.markdown('<p class="font">Object Detection App For Your Safety</p>', unsafe_allow_html=True)
with st.sidebar.expander("About the App"):
     st.write("""
        Use this simple app to find out details about the picture taken .  \n  \nThis app was created by a group of students of vnrvjiet (soumya, abhay, sufiya, omega) . Hope you enjoy!
     """)  
        
        
file_image = st.camera_input(label = "Take a pic of you to be sketched out")

if file_image:
    input_img = Image.open(file_image)
    st.write("**Input Photo**")
        st.image(input_img, use_column_width=True)
        
else:
     st.write("You haven't uploaded any image file")        
