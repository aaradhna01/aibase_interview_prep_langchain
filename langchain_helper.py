import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

def get_answer_from_ai(question):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    messages = [
        SystemMessage(content="You are an expert job interview assistant. Give smart and confident answers."),
        HumanMessage(content=question)
    ]

    response = llm(messages)
    return response.content
