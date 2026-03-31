import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage

hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=hf_token,
    task="conversational",   # 🔥 IMPORTANT FIX
    max_new_tokens=300
)

chat = ChatHuggingFace(llm=llm)

st.title("Chat App 💬")

text = st.text_input("Ask something")

if text:
    response = chat.invoke([HumanMessage(content=text)])
    st.write(response.content)
