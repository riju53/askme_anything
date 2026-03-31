import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint

hf_token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

llm = HuggingFaceEndpoint(
    #repo_id="google/flan-t5-base",
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token=hf_token,
    temperature=0.1,
    max_new_tokens=300
)

st.title("Ask me anything 🚀")

with st.form('my_form'):
    text = st.text_area('Enter text:')
    submit = st.form_submit_button('Ask')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            try:
                response = llm.invoke(text)

                # ✅ handle empty response (important)
                if response:
                    st.success(response)
                else:
                    st.warning("No response from model. Try again.")

            except Exception as e:
                st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a question!")
