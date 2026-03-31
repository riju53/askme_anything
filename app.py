import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint

hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    huggingfacehub_api_token=hf_token,
    temperature=0.7,
    max_new_tokens=256
)

# Streamlit UI
st.title("Askme anything 🚀")

with st.form('my_form'):
    text = st.text_area('Enter text:', '...')
    submit = st.form_submit_button('Ask')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            response = llm.invoke(text)
            st.success(response.content)
    else:
        st.warning("Please enter a question!")
