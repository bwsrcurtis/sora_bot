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


messages= []
responses = []
@app.route('/', methods=('GET', 'POST'))
def hello_world():
    if request.method=='POST':
        message = request.form['message']
        messages.append(message)
        response = query(message)["generated_text"]
        responses.append(response)
        conversation_dict = list(zip(messages, responses))
        # conversation_dict.reverse()
        return render_template('index.html', conversation_dict=conversation_dict[:5])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()