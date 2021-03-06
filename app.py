# from cProfile import run
import streamlit as st
from tkinter import Menu
from app_eda import run_eda

from app_home import run_home
from app_ml import run_ml



def main():

    st.title('건강상태 예측해서 사전에 알려주기')
    st.sidebar.image('data/의사.jpg',use_column_width=True)
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()


if __name__ == '__main__' :
    main()