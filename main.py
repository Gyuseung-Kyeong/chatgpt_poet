from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import streamlit as st


load_dotenv()

chat_model = ChatOpenAI()

st.title("인공지능 시인")
content = st.text_input("시의 주제")


def generate_poem():
    with st.spinner("시를 작성하는 중입니다..."):
        result = chat_model.predict(f"{content}에 대한 시를 써줘")
        st.write(result)
    print(f"content: {content}")
    print(result)


if content or st.button("시 작성 요청하기"):
    generate_poem()
