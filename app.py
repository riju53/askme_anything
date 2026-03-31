import streamlit as st
from langchain_community.llms import HuggingFaceHub

#hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    huggingfacehub_api_token=hf_token,
    model_kwargs={
        "temperature": 0.7,
        "max_length": 256
    }
)
st.title("Askme anything 🚀")

with st.form('my_form'):
    text = st.text_area('Enter text:')
    submit = st.form_submit_button('Ask')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            st.write("Model loded")
            response = llm.invoke(text)
            st.success(response)
    else:
        st.warning("Please enter a question!")
