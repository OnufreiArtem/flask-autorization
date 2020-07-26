from flask import Flask, render_template, request, redirect, url_for, session
from dbcontroller import check_auth
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    if not session.get('logged_in'):
        return redirect('login')
    else:
        return "Hello Boss!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect('home')

    if request.method == "POST":
        if check_auth(request.form['username'], request.form['password']):
            session['logged_in'] = True
            return redirect('/')
        else:
            return redirect('login')
    else: 
        return render_template('index.html')
    
    




if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)