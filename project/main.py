# Standard Library Imports
from random import randint

# Third Party Imports
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session

# imports from .py files
from house import house
from class_admin import Admin
from class_guest import Guest
from class_staff import Staff
from class_passcode import Passcode
from class_activation import Activation

from configuration_app import app
from configuration_log import info_logger, error_logger
from configuration_form import check_password, RegistrationForm, LoginForm, NewGuestForm, NewStaffForm, HousePasscodeForm 

# require login config
def require_login(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		# if there isn"t a logged user
		if not session.get("SIGNED_IN"):
			return redirect("/login")
		return func(*args, **kwargs)
	return wrapper


# register page
@app.route("/register", methods=["GET", "POST"])
def register():
	# defined in form_config.py
	form = RegistrationForm()

	form.passcode.data = randint(10000000, 99999999)

	# if form is valid
	if form.validate_on_submit():
		# get value and create user
		admin_values = (
			None,
			request.form["username"],
			request.form["name"],
			request.form["surname"],
			Admin.hash_password(request.form["password"]),
			request.form["passcode"],
		)

		Admin(*admin_values).create()

		passcode_value = (
			None,
			request.form["passcode"],
			"forever",
			"forever"
		)

		Passcode(*passcode_value).create()

		Activation.activate(request.form["key"])

		# get the user and put him in the session
		session["SIGNED_IN"] = True
		session["USERNAME"] = request.form["username"]

		# success log
		info_logger.info("%s registered successfully", request.form["username"])

		return redirect("/")

	else:
		# error log
		if request.method == "POST":
			error_logger.error("Failed registration!")

	# template the registration form
	return render_template("admin/register.html", form = form)


# login page
@app.route("/login", methods=["GET", "POST"])
def login():
	# defined in form_config.py
	form = LoginForm()

	# if form is valid
	if form.validate_on_submit():
		# get the user and put him in the session
		session["SIGNED_IN"] = True
		session["USERNAME"] = request.form["username"]

		# success log
		info_logger.info("%s logined in successfully", request.form["username"])

		return redirect("/")

	else:
		# error log
		if request.method == "POST":
			error_logger.error("Failed login!")
	
	# template the login form
	return render_template("admin/login.html", form = form)


# logout page
@app.route("/logout")
@require_login
def logout():
	# success log
	info_logger.info("%s logged out successfully", session.get("USERNAME"))

	# remove user from the session
	session["SIGNED_IN"] = False
	session["USERNAME"] = None

	return redirect("/")

@app.route("/profile", methods=["GET"])
@require_login
def profile():
	admin = Admin.find_by_username(session.get("USERNAME"))

	# template the registration form
	return render_template("admin/profile.html", admin = admin)

@app.route("/new_guest", methods=["GET", "POST"])
@require_login
def new_guest():
	form = NewGuestForm()

	form.passcode.data = randint(10000000, 99999999)

	if form.validate_on_submit():
		
		guest_values = (
			None,
			request.form["name"],
			request.form["surname"],
			request.form["phone_number"],
			request.form["passcode"],
			request.form["entry_date"],
			request.form["expiry_date"]
		)

		Guest(*guest_values).create()

		passcode_value = (
			None,
			request.form["passcode"],
			request.form["entry_date"],
			request.form["expiry_date"]
		)

		Passcode(*passcode_value).create()

		info_logger.info("Guest successfully created.")

		return redirect("/guests")

	else:
		if request.method == "POST":
			error_logger.error("Guest couldn't be created!")

	return render_template("guests/new_guest.html", form = form)

@app.route("/new_staff", methods=["GET", "POST"])
@require_login
def new_staff():
	form = NewStaffForm()

	form.passcode.data = randint(10000000, 99999999)

	if form.validate_on_submit():
		
		staff_values = (
			None,
			request.form["name"],
			request.form["surname"],
			request.form["phone_number"],
			request.form["position"],
			request.form["passcode"]
		)

		Staff(*staff_values).create()

		passcode_value = (
			None,
			request.form["passcode"],
			"forever",
			"forever"
		)

		Passcode(*passcode_value).create()

		info_logger.info("Staff successfully created.")

		return redirect("/staff")

	else:
		if request.method == "POST":
			error_logger.error("Staff couldn't be created!")

	return render_template("staff/new_staff.html", form = form)

@app.route("/guests", methods=["GET"])
@require_login
def guests():
	guests = Guest.all()
	return render_template("guests/guests.html", guests = guests)

@app.route("/staff", methods=["GET"])
@require_login
def staff():
	staff = Staff.all()
	return render_template("staff/staff.html", staff = staff)

if __name__ == '__main__':
	app.run(debug=True, port=80, host='0.0.0.0')
