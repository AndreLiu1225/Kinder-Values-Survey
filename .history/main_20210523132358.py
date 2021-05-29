from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class MCQ(FlaskForm):