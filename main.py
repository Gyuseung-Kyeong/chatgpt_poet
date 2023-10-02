from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import streamlit as st


load_dotenv()

chat_model = ChatOpenAI()


st.header("사랑에 힘들어하는 시인")
st.write("네 마음의 문제나 느낌을 알려줘. 나는 그것을 시로 변환해 줄 거야.")

# Dropdown for type of relationship issue
issue_type = st.selectbox("어떤 종류의 연애 문제야?", ["선택하세요", "이별", "질투", "소통 문제", "거리 두기", "기타"])

# Multiselect for feelings involved
feelings = st.multiselect("이 문제와 관련된 느낌은 무엇인가요?", ["슬픔", "화남", "무관심", "헷갈림", "기쁨", "기타"])

# Text input for any additional information or specifics
content = st.text_input("더 자세한 이야기나 느낌을 공유해주세요:")

# When the button is pressed or enter is hit after input
if content or st.button("시 작성 요청하기"):
    # Generate a poem using all the information provided
    poem_request = f"{issue_type} 문제와 {', '.join(feelings)} 느낌에 대한 시를 써줘. {content}"
    with st.spinner("시를 작성하는 중입니다..."):
        result = chat_model.predict(poem_request)
        st.write(result)
        print("poem_request: ", poem_request)
        print("result: ", result)
