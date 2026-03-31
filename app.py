import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    huggingfacehub_api_token=hf_token,
    temperature=0.7,
    max_new_tokens=256
)
model = ChatHuggingFace(llm=llm)

st.title("Askme anything 🚀")

with st.form('my_form'):
    text = st.text_input('Enter text:')
    submit = st.form_submit_button('Ask me')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            st.write("Model loded")
            response = model.invoke(text)
            st.write(response.content)
    else:
        st.warning("Please enter a question!")
