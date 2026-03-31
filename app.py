import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint

hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

from langchain_huggingface import ChatHuggingFace

llm = ChatHuggingFace(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=hf_token
)

# Streamlit UI
st.title("Askme anything 🚀")

with st.form('my_form'):
    text = st.text_area('Enter text:')
    submit = st.form_submit_button('Ask')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            st.write("Model loaded successfully")
            response = llm.invoke(text)
            st.success(response.content)
    else:
        st.warning("Please enter a question!")
