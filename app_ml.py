import streamlit as st
import numpy as np
import sklearn

import joblib

def run_ml():
    st.subheader('심장질환 예측하기')

    # 예측하기 위해서 필요한 파일들을 불러와야 된다.
    # 이 예에서는, 인공지능파일, X 스케일러 파일, y 스케일러파일
    # 3개를 불러와야 한다.

    regressor = joblib.load('data/classifier1.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y =joblib.load('data/scaler_y.pkl')

    HeartDisase = st.radio('심장질환을 유무를 선택해주세요.',['있다','없다'])
    if HeartDisase == '있다' :
        gender = 1
    else :
        gender = 0
    Smoking = st.radio('흡연 유무를 선택해주세요.',['흡연','비흡연'])
    if HeartDisase == '흡연' :
        gender = 1
    else :
        gender = 0
    AlcoholDrinking = st.radio('음주하는지에 대한 유무를 선택해주세요.',['음주','금주'])
    if AlcoholDrinking == '음주' :
        gender = 1
    else :
        gender = 0
    debt = st.number_input('카드빛 입력',0)
    worth = st.number_input('자산 입력',0)
