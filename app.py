from fastapi import FastAPI, APIRouter
from flask import Flask, request, session, g, Blueprint
from langchain_openai import ChatOpenAI
from agent import LoginAgent, NonLoginAgent
from dotenv import load_dotenv
import os
import asyncio


app = Flask(__name__)

load_dotenv()
api = os.getenv('OPENAPI')
os.environ['OPENAI_API_KEY'] = api

llm_model = ChatOpenAI(
    temperature=0.0,
    max_tokens=2048,
    model_name="gpt-4o-mini"
)
db = "mysql+pymysql://root:1234@localhost:3306/chat_history"


@app.route('/chat', methods = ['POST'])
def get_id():
    response = request.form['email']
    return response
    

user_id = get_id()

try:
    chatbot = LoginAgent(llm_model, db_path = db, user_id = user_id)
except TypeError:
    chatbot = NonLoginAgent(llm_model)

# login = LoginAgent(llm_model, db_path = db, user_id = user_id)
# non = NonLoginAgent(llm_model)


@app.route('/chat/login', methods = ['POST'])
def chat():
    question = request.form['input']
    response = chatbot.answer_to_me(question)
    print(response['output'])
    return response['output']

@app.route('/chat/non', methods = ['POST'])
def chat_non():
    question = request.form['input']
    response = chatbot.answer_to_me(question)
    print(response['output'])
    return response['output']
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000)