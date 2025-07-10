from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello World!"
@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

@app.route('/success/<score>')
def success(score):
    return "Hey your marks are " + score

if __name__ == '__main__':
        app.run(debug=True)