from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/birthday')
def birthday():
    return 'October 13 1986'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' +  name + '!'