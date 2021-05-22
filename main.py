from joblib import *
import numpy as np
import streamlit as st
model=load('Kumar.ml')
st.image('1.PNG')
st.title('How much calories have you burnt during your exercise ?')
st.write('Find out !!')
def home():
    gen=[0,1]
    ge=['Female','Male']
    gender=st.selectbox('Gender',gen,format_func=lambda x:ge[x])
    age=st.number_input('Enter your Age',min_value=0,max_value=200,step=1)
    height= st.number_input('Enter your height(cm)', min_value=0, max_value=200, step=1)
    weight = st.number_input('Enter your weight(kg)', min_value=0, max_value=200, step=1)
    dur= st.number_input('Enter duration of your exercise (mins)', min_value=0, max_value=200, step=1)
    hb = st.number_input('Enter the heart rate', min_value=0, max_value=200, step=1)
    bt = st.number_input('Enter your body temperature', min_value=0, max_value=200, step=1)
    b=st.button('Calories Burnt')
    if b:
        y_pred=np.round(model.predict([[gender,age,height,weight,dur,hb,bt]]),2)
        st.success('Calories Burnt:{}'.format(y_pred[0]))

if __name__ == '__main__':
    home()