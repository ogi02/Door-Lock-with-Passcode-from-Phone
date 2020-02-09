# python imports
from flask import Flask, render_template, request, redirect, url_for, session
#from datetime import datetime
from functools import wraps
import os

# imports from .py files
#from user import User
#from task import Task
#from log_config import info_logger, error_logger
#from form_config import check_password, RegistrationForm, EditProfileForm, LoginForm, TaskForm

# app config
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

# require login config
def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # if there isn't a logged user
        if not session.get("SIGNED_IN"):
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper


# main page
@app.route("/")
def hello():
    return render_template("index.html")


# register page
@app.route("/register", methods=["GET", "POST"])
def register():
    # defined in form_config.py
    form = RegistrationForm()

    # if form is valid
    if form.validate_on_submit():
        # get value and create user
        values = (
            None,
            request.form["username"],
            request.form["email"],
            User.hash_password(request.form["password"])
        )
        User(*values).create()

        # get the user and put him in the session
        user = User.find_by_email(request.form["email"])
        session["SIGNED_IN"] = True
        session["EMAIL"] = request.form["email"]

        # success log
        info_logger.info("%s registered successfully", request.form['email'])

        return redirect("/tasks")

    else:
        # error log
        if request.method == "POST":
            error_logger.error("%s failed to register", request.form["email"])

    # template the registration form
    return render_template("register.html", form=form)
