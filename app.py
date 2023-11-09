import streamlit as st
import pandas as pd
import numpy as np
# from process import ordinal,manualOrdinal,get_prediction
import pickle

st.set_page_config(page_title="Smartphone Price Prediction App",
                   page_icon="📱", layout="wide")

with open('model/tune_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('data/dictionary.pkl', 'rb') as f:
    dct = pickle.load(f)

option_brand = ['OnePlus', 'Samsung', 'Motorola', 'Realme', 'Apple', 'Xiaomi',
       'Nothing', 'Oppo', 'Vivo', 'OPPO', 'Poco', 'iQOO', 'Jio', 'Gionee',
       'Tecno', 'Infinix', 'Cola', 'Letv', 'POCO', 'iKall', 'LeEco',
       'Nokia', 'Lava', 'Honor', 'Nubia', 'Redmi', 'Asus', 'itel',
       'Google', 'Sony', 'Oukitel', 'BLU', 'Lyf', 'Huawei', 'ZTE',
       'Lenovo', 'Micromax', 'LG', 'Doogee', 'Itel', 'TCL', 'Sharp',
       'Blackview']

option_os = ['android', 'ios', 'other']

option_processor_brand = list(dct.keys())

st.markdown("<h1 style='text-align: center;'>Smartphone Price Prediction App 📱</h1>", unsafe_allow_html=True)
def main():
    with st.form('predictin_form'):
        st.subheader("Enter the below Features:")

        pro_brand = st.selectbox("Select Processor Brand: ",options=option_processor_brand)        
        pro = st.selectbox("Select Processor Name: ",options=dct[pro_brand])


        submit_1=st.form_submit_button("Predict")
    
    with st.form('predictin_form_1'):
        st.subheader("Enter the below Features:")

        pro_brand = st.selectbox("Select Processor Brand: ",options=option_processor_brand)
        pro = st.selectbox("Select Processor Name: ",options=dct[pro_brand])


        submit_2=st.form_submit_button("Predict")
    if submit_1:
        pass
    if submit_2:
        pass
    

if __name__=='__main__':
    main()