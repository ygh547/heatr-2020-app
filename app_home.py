from PIL import Image
import streamlit as st

def run_home():
    st.subheader('이 앱은 심장질환 예측하는 데이터에 대한 내용입니다.')
    st.text('왼쪽 사이드바에서 원하는 항목을 선택하세요.')

    img = Image.open('data/심장질환 진당가능.jpg')

    st.image(img,use_column_width=True)
