# Standard Library Imports
from datetime import date

# Third Party Imports
from flask import render_template, request

# Local imports
from class_passcode import Passcode
from configuration_app import app
from configuration_form import HousePasscodeForm

# Imports for LEDs
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RedLightPin = 21
GreenLightPin = 15

GPIO.setup(RedLightPin, GPIO.OUT)
GPIO.output(RedLightPin, False)
GPIO.setup(GreenLightPin, GPIO.OUT)
GPIO.output(GreenLightPin, False)

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
			GPIO.output(GreenLightPin, True)
			time.sleep(1)
			GPIO.output(GreenLightPin, False)
		else:
			print("ne vlezna")
			GPIO.output(RedLightPin, True)
			time.sleep(1)
			GPIO.output(RedLightPin, False)

	return render_template("index.html", form = form)
