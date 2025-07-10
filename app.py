from flask import Flask,render_template,request
from socket import gethostname
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello World!"
@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')
if __name__ == '__main__':
        app.run(debug=True)