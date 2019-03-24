import json
from flask import Flask

app = Flask(__name__)

messages = ['Hello World!']

@app.route('/')
def index():
    return json.dumps(messages)

@app.route('/add/<message>')
def add (message):
    messages.append(message)

    return 'Added message!'


if __name__ == '__main__':
    app.run()