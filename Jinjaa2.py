from flask import Flask,render_template,request,redirect,url_for

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
# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}'
#     return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    rslt=""
    if(score)>=55:
        rslt="Passed"
    else:
        rslt="Failed"
    return render_template('marks.html',results=rslt)

@app.route('/success2/<int:score>')
def success2(score):
    rslt=""
    if(score)>=55:
        rslt="Passed"
    else:
        rslt="Failed"
    abc={"Score":score,"Rslt":rslt}
    return render_template('marks1.html',results=abc)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('marks.html',results=score)

@app.route('/fail')
def successiffail(score):
    return render_template('result.html',results=score)
@app.route('/submitt',methods=['GET','POST'])
def submitt():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        datascience=float(request.form['datascience'])
        AI=float(request.form['ai'])
        total_score=maths+datascience+AI+science
        total_score/=4
    else:
        return render_template('getresult.html')
    return redirect(url_for('success2',score=total_score))
if __name__ == '__main__':
        app.run(debug=True)