from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import InputRequired, EqualTo, Length, NoneOf, ValidationError

from class_admin import Admin
from class_activation import Activation

# check valid key activation
def validate_key(form, key):
    activation = Activation.get_by_key(request.form["key"])

    if not activation or activation.active:
        raise ValidationError("Incorrect Key!")

# registration form
class RegistrationForm(FlaskForm):
    # name -> input type - string, required
    name = StringField("name", [InputRequired()])

    # surname -> input type - string, required
    surname = StringField("surname", [InputRequired()])

    # username -> input type - string, required, unique
    username = StringField("username", [InputRequired(), NoneOf(Admin.all_usernames(), message = "An admin with this username already exists!")])

    # password -> input type - password, required, at least 8 characters long
    password = PasswordField("password", [InputRequired(), Length(min = 8, message = "Password must be at least 8 characters!")])

    # confirm -> input type - password, equal to password
    confirm = PasswordField("confirm", [EqualTo("password", message = "Passwords must match!")])

    # key -> input type - string, required, validated
    key = StringField("key", [InputRequired(), validate_key])

    # passcode -> input type - string, passcode for entering
    passcode = StringField("passcode")

# check login password
def check_password(form, password):
    # get admin trying to log in
    admin = Admin.find_by_username(request.form["username"])

    # if user exists and his password is correct
    if not admin or not admin.verify_password(password.data):
        raise ValidationError("Incorrect Username or Password!")

# login form
class LoginForm(FlaskForm):
    # username -> input type - string, required
    username = StringField("username", [InputRequired(message = "Username is required!")])

    # password -> input type - password, verification if password is correct in db
    password = PasswordField("password", [InputRequired(message = "Password is required"), check_password])

class NewGuestForm(FlaskForm):
    # name -> input type - string, required
    name = StringField("name", [InputRequired(message = "Name is required")])
    
    # surname -> input type - string, required
    surname = StringField("surname", [InputRequired(message = "Surname is required")])
    
    # phone number -> input type - string, required
    phone_number = StringField("phone_number", [InputRequired(message = "Phone number is required")])
    
    # passcode -> input type - string, readonly
    passcode = StringField("passcode")
    
    # entry date -> input type - date, required
    entry_date = DateField("entry_date", format='%Y-%m-%d')
    
    # expiry date -> input type - date, required
    expiry_date = DateField("expiry_date", format='%Y-%m-%d')

class NewStaffForm(FlaskForm):
    # name -> input type - string, required
    name = StringField("name", [InputRequired(message = "Name is required")])
    
    # surname -> input type - string, required
    surname = StringField("surname", [InputRequired(message = "Surname is required")])

    # phone number -> input type - string, required
    phone_number = StringField("phone_number", [InputRequired(message = "Phone number is required")])

    # position -> input type - string, required
    position = StringField("position", [InputRequired(message = "Position is required")])

    # passcode -> input type - string, readonly
    passcode = StringField("passcode")

class HousePasscodeForm(FlaskForm):
    # passcode -> input type - string, readonly, inputted through buttons with numbers
    passcode = StringField("passcode")