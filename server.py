from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if not 'counter' in session:
        session['counter'] = 1
    else:
        # print session['counter']
        session['counter'] = session['counter']+1
        # return session['counter']
        # session['counter'] = 1
    # return session['counter']
        # raise ConnectionError("no session")

    # session['counter']= session['counter']+1
    return render_template("index.html")
    # return render_template("index.html", counter = session['counter'])

@app.route('/signout',methods= ['POST'])
def sign_out():
    # button = request.form['button']
    # session['counter']=0
    session.pop('counter')
    return redirect('/')

@app.route('/2')
# def counter():
def double():
    session['counter']= session['counter']+2
    return render_template("index.html", counter = session['counter'])

#     counter = counter + 1
#     return render_template("index.html", counter = counter)

#
# @app.route('/show')
# def show_user():
#   return render_template('users.html', name='Jay', email='kpatel@codingdojo.com')


app.run(debug=True)
