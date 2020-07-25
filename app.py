from flask import Flask, render_template, request, redirect, url_for, session
from dbcontroller import check_auth
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return "Hello Boss!"


@app.route('/login', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        if check_auth(request.form['username'], request.form['password']):
            session['logged_in'] = True
            print("Yes")
        else:
            print("No") 
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)