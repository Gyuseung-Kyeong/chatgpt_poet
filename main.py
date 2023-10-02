from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import streamlit as st


load_dotenv()

chat_model = ChatOpenAI()

st.title("실연당한 시인")
content = st.text_input("어떤 연애 문제가 있어? 네 마음을 시로 표현해 줄께")


def generate_poem():
    with st.spinner("너의 감정을 들여다 보고 있어. 조금만 기다려줘."):
        direction = """
        {content}에 대한 시를 써줘.
        연인과 이별한 상황을 가정하고 애절한 시를 써줘."
        """
        result = chat_model.predict(direction)
        st.write(result)
    print(f"content: {content}")
    print(result)
