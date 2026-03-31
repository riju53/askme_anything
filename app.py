import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load token securely
hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

# Use a PUBLIC model (important)
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    huggingfacehub_api_token=hf_token,
    temperature=0.1,
    max_new_tokens=500
)

model = ChatHuggingFace(llm=llm)

# UI
st.title("Ask me anything 🚀")

with st.form('my_form'):
    text = st.text_area('Enter text:')
    submit = st.form_submit_button('Ask')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            response = llm.invoke(text)
            st.success(response)
    else:
        st.warning("Please enter a question!")
