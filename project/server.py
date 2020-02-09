from flask import Flask
from flask import render_template, request, redirect, url_for
from admin import Admin

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        if request.form['password'] == request.form['repeat_password']:
            values = (None, request.form['username'], request.form['name'], request.form['surname'], request.form['password'], request.form['passcode'])
            Admin(*values).create()
            return redirect(url_for('hello'))
        else:
            # exception of some kind
            return render_template('sth.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
