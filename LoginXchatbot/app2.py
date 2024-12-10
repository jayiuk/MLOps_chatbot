from fastapi import FastAPI, APIRouter
from flask import Flask, request, session, g, Blueprint
from langchain_openai import ChatOpenAI
from agent import NonLoginAgent
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
api = os.getenv('OPENAPI')
os.environ['OPENAI_API_KEY'] = api

llm_model = ChatOpenAI(
    temperature=0.0,
    max_tokens=2048,
    model_name="gpt-4o-mini"
)

chatbot = NonLoginAgent(llm_model)

@app.route('/chat/non', methods = ['POST'])
def chat_non():
    question = request.form['input']
    response = chatbot.answer_to_me(question)
    return response['output']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000)