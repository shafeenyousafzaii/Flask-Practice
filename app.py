from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello World!"
@app.route('/index')
def index():
    return('template/index.html')
