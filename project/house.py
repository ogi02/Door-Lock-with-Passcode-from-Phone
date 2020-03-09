# Standard Library Imports
from datetime import date

# Third Party Imports
from flask import render_template, request

# Local imports
from class_passcode import Passcode
from configuration_app import app
from configuration_form import HousePasscodeForm

# main page
@app.route("/", methods=["GET", "POST"])
def house():
	form = HousePasscodeForm()

	form.passcode.data = 0

	if form.validate_on_submit():
		value = request.form["passcode"]
		passcode = Passcode.get_by_passcode(value)
		now = date.today().strftime("%Y-%m-%d")
		if passcode and ((passcode.entry_date < now and now < passcode.expiry_date) or passcode.entry_date == "forever"):
			print("vlezna")
		else:
			print("ne vlezna")

	return render_template("index.html", form = form)