import pandas as pd
import streamlit as st
import pickle as pkl
from pickle import dump
from pickle import load
from sklearn.ensemble import RandomForestRegressor

st.title('welcome to project 189')

def user_inp():
        ambient = st.number_input('ambient', key="1")
        coolant = st.number_input('coolant', key="2")
        u_d = st.number_input('u_d', key="3")
        u_q = st.number_input('u_q', key="4") 
        i_d = st.number_input('i_d', key="5")
        i_q = st.number_input('i_q', key="6")
        pm = st.number_input('pm', key="7")
        stator_yoke = st.number_input('stator_yoke', key="8")
        stator_tooth = st.number_input('stator_tooth',key="9")
        stator_winding = st.number_input('stator_winding',key="10")

        data = {'ambient':ambient,
                'coolant':coolant,
                'u_d':u_d,
                'u_q':u_q,
                'i_d':i_d,
                'i_q':i_q,
                'pm':pm,
                'stator_yoke':stator_yoke,
                'stator_tooth':stator_tooth,
                'stator_winding':stator_winding}
        
        features = pd.DataFrame(data,index = [0])
        return features

df = user_inp()
st.write(df)

loaded_model = pkl.load(open('C:\\Users\\bodak\\Downloads\\model_pickle','rb'))
pred_model = loaded_model.predict(df)

st.subheader('predicted motor speed')
st.write(pred_model)
