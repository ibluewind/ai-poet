# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
import streamlit as st

model = ChatOpenAI()

st.title('인공지능 시인')
title = st.text_input(label='시의 주제:', placeholder='시의 주제를 제시해주세요')
st.write('시의 주제는 ', title)

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):
        result = model.predict(title + "에 대한 시를 써줘")
        st.write(result)