import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# =====================================
# 🔐 API KEYS (PUT YOUR KEYS HERE)
# =====================================

os.environ["GOOGLE_API_KEY"] = "gemini api"

# Optional LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your langchin api"

# =====================================
# 🧠 Prompt Template
# =====================================

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are Gemini 2.5 Flash, a smart AI assistant. Answer clearly and helpfully."),
        ("user", "Question: {question}")
    ]
)

# =====================================
# 🤖 Gemini Model
# =====================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    max_output_tokens=1024
)

# Output parser
output_parser = StrOutputParser()

# LangChain pipeline
chain = prompt | llm | output_parser

# =====================================
# 🎨 Streamlit UI
# =====================================

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Gemini 2.5 Flash Chatbot")
st.write("Powered by **LangChain + Gemini + Streamlit**")

input_text = st.text_input("💬 Ask me anything:")

# =====================================
# 💬 Response Logic
# =====================================

if input_text:

    with st.spinner("🤔 Thinking..."):

        try:
            response = chain.invoke({"question": input_text})

            st.success("✅ Response")
            st.write(response)

        except Exception as e:
            st.error(f"Error: {str(e)}")