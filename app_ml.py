from itertools import tee
from matplotlib.pyplot import axis, text
import streamlit as st
import numpy as np
import pandas as pd
import sklearn

import joblib
from traitlets import CInt



def run_ml():
    st.subheader('심장질환 예측하기')

    heart_df = pd.read_csv('data/heart_2020.csv',index_col=0,encoding='ISO-8859-1')
    # 예측하기 위해서 필요한 파일들을 불러와야 된다.
    # 이 예에서는, 인공지능파일, X 스케일러 파일, y 스케일러파일
    # 3개를 불러와야 한다.

    regressor = joblib.load('data/classifier1.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y =joblib.load('data/scaler_y.pkl')

    HeartDisase = st.radio('심장질환을 유무를 선택해주세요.',['있다','없다'])
    if HeartDisase == '있다' :
        HeartDisase = 1
    else :
        HeartDisase = 0
    Smoking = st.radio('흡연 유무를 선택해주세요.',['흡연','비흡연'])
    if HeartDisase == '흡연' :
        Smoking = 1
    else :
        Smoking = 0
    AlcoholDrinking = st.radio('음주하는지에 대한 유무를 선택해주세요.',['음주','금주'])
    if AlcoholDrinking == '음주' :
        AlcoholDrinking = 1
    else :
        AlcoholDrinking = 0
    Stoke = st.radio('과거부터 현재까지 뇌졸중질병 유무를 선택해주세요.',['있다','없다'])
    if Stoke == '있다' :
        Stoke = 1
    else :
        Stoke = 0
    age = st.number_input('나이 입력',0,120)
    if age > 70 :
        age = 1
    else :
        age = 0

    if st.button('심장병 예측') : 

        # 1. 신규 고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([HeartDisase,Smoking,AlcoholDrinking,Stoke,age])

        # 2. 학습할때 사용한 X 의 피처 스케일러를 이용해서, 피처스케일링하기
        # 먼저, 데이터를 2차원으로 만들어준다.
        new_data = new_data.reshape(1, 5)
        new_data = scaler_X.transform(new_data)

        # 3. 인공지능에게 예측해달라고 한다.
        y_pred = regressor.predict(new_data)
        
        # 4. 예측한 값을, 원상복구 시킨다.
        y_pred = scaler_y.inverse_transform(y_pred)

        y_pred = round(y_pred[0,0])
        st.write('당신의 점수는'+ str(y_pred) + '점입니다.')    
    

    


    
    
    

    # worth = st.number_input('자신이 속한 나이를 선택해주세요.',0)
