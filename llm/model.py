from langchain_openai import ChatOpenAI
import os

def get_llm():
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.3,
        api_key=os.environ.get("OPENAI_API_KEY")
    )
