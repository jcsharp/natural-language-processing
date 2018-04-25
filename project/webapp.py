from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from utils import *
from dialogue_manager import DialogueManager
import re

app = Flask(__name__)

dm = DialogueManager(RESOURCE_PATH)
urlre = re.compile(r"(^|[\n ])(([\w]+?://[\w\#$%&~.\-;:=,?@\[\]+]*)(/[\w\#$%&~/.\-;:=,?@\[\]+]*)?)", re.IGNORECASE | re.DOTALL)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    answer = str(dm.generate_answer(userText))
    answer = urlre.sub(r'\1<a href="\2" target="_blank">\2</a>', answer)
    return answer


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
