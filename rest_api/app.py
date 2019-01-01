from flask import Flask

app = Flask(__name__)

@app.route('/') # https://google.com/
def home():
    return "Hello World"

app.run(port=5000)