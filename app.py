import streamlit as st
from process import process_encode, encode_YN
import pickle

st.set_page_config(page_title="Smartphone Price Prediction App",
                   page_icon="📱", layout="wide")

with open('data/lable_brand.pkl', 'rb') as f:
    lable_brand = pickle.load(f)
with open('data/lable_os_type.pkl', 'rb') as f:
    lable_os_type = pickle.load(f)
with open('data/lable_processor_name.pkl', 'rb') as f:
    lable_processor_name = pickle.load(f)

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

option_ram = [12.,  6.,  4.,  8.,  3., 16.,  2., 18.,  1.]
option_rom = [256., 128.,  64.,  32., 512.,  16.,   8.]
option_refresh_rate = [120,  90,  60, 144, 165]
option_screen_resoltion = [1440., 1080.,  720., 2200.]
option_rear_cam = [16., 13.,  8., 12., 32.,  5., 50., 40., 10., 60.,  2.,  7., 44.,
       20., 24., 25.]
option_front_cam = [16., 13.,  8., 12., 32.,  5., 50., 40., 10., 60.,  2.,  7., 44.,
       20., 24., 25.]




option_processor_brand = list(dct.keys())

st.markdown("<h1 style='text-align: center;'>Smartphone Price Prediction App 📱</h1>", unsafe_allow_html=True)
def main():
    with st.form('predictin_form'):
        st.subheader("Enter the below Features:")

        brand = st.selectbox("Select Mobile Brand: ",options=option_brand)
        processsor_brand = st.selectbox("Select Processor Brand: ",options=option_processor_brand)        
        
        submit_1=st.form_submit_button("Select")
    if submit_1:
        processsor_brand = processsor_brand
        # brand = process_encode(brand, lable_brand)
    
    with st.form('predictin_form_1'):
        processsor_name = st.selectbox("Select Processor Name: ", options=dct[processsor_brand])
        net_5g = st.selectbox("5G", options=['Yes', 'No'])
        clock_speed = st.slider("Pickup Clock Speed: ", 1.2, 3.2, format="%.1f")
        ram = st.selectbox("Select RAM Size:", options=option_ram)
        rom = st.selectbox("Select Storage Capacity:", options=option_rom)
        mah = st.slider("Select Battry Capacity:", 1800, 22000, format="%d")
        charge = st.slider("Select Charging Speed:", 2, 240, format='%d')
        screen_size = st.slider("Select Screen Size:", 4.7, 7.0, format="%.1f")
        screen_resoltion = st.selectbox("Select Screen Resolution:", options=option_screen_resoltion)
        refresh_rate = st.selectbox("Select Screen Refresh Rate:", options=option_refresh_rate)
        rear_cam = st.select_slider("Select Rear Camera Quality:", options=option_rear_cam)
        front_cam = st.select_slider("Select Front Camera Quality:", options=option_front_cam)
        memory_card = st.selectbox("Select Memory Card Needed or Not:", options=['Yes', 'No'])
        os = st.selectbox("Select OS Tyep:", options=option_os)

        submit_2 = st.form_submit_button("Predict")
    
    if submit_2:
        processsor_name = process_encode(processsor_name, lable_processor_name)
        net_5g = encode_YN(net_5g)
        clock_speed = clock_speed
        ram = ram
        rom = rom
        mah = mah
        charge = charge
        screen_size = screen_size
        screen_resoltion = screen_resoltion
        refresh_rate = refresh_rate
        rear_cam = rear_cam
        front_cam = front_cam
        memory_card = encode_YN(memory_card)
        os = process_encode(os, lable_os_type)
        brand = process_encode(brand, lable_brand)


        values = [brand, net_5g, processsor_name, clock_speed, ram, rom, mah, charge, screen_size, refresh_rate, 
                  screen_resoltion, rear_cam, front_cam, memory_card, os]
        
        pred = model.predict([values])

        st.write(f"The predicted Cell Phone price is:  {round(pred[0])}")
    

if __name__=='__main__':
    main()