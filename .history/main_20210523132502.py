from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class MCQ(FlaskForm):
    age = IntegerField("Age", [DataRequired])