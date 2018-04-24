from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from utils import *
from dialogue_manager import DialogueManager

app = Flask(__name__)

dm = DialogueManager(RESOURCE_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(dm.generate_answer(userText))


if __name__ == "__main__":
    app.run()
