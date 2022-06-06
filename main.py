from flask import Flask, render_template, request
import json
import requests
from config import api_key
API_URL = "https://api-inference.huggingface.co/models/CurtisBowser/DialoGPT-medium-sora"
headers = {"Authorization": f"Bearer {api_key}"}


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def hello_world():
    if request.method=='POST':
        message = request.form['message']
        response = query(message)["generated_text"]
        conversation_dict = (message, response)
        return render_template('index.html', message=conversation_dict[0], response=conversation_dict[1])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()