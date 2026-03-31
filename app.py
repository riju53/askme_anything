import streamlit as st
from langchain_community.llms import HuggingFaceHub

hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

llm = HuggingFaceHub(
    repo_id="bigscience/bloom-560m",
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
            try:
                response = llm.invoke(text)
                st.success(response)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a question!")
