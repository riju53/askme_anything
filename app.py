import os
import streamlit as st

import os
os.environ["HUGGINGFACEHUB_API_TOKEN"]="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"

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Initialize model
llm = HuggingFaceEndpoint(
    #repo_id="meta-llama/Llama-3.1-8B-Instruct",
    repo_id="google/flan-t5-base",
    temperature=0.1,
    max_new_tokens=500
)

model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.title("Askme anything 🚀")

with st.form('my_form'):
    text = st.text_area('Enter text:', '...')
    submit = st.form_submit_button('Ask')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            response = model.invoke(text)
            st.success(response.content)
    else:
        st.warning("Please enter a question!")
