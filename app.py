from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        team = request.form["teamName","teamlogo","github"]
        return redirect(url_for("team",team=team))
    else:
        return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)