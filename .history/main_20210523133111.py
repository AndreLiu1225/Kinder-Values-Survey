from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class MCQ(FlaskForm):
    age = IntegerField("Age", [DataRequired()])
    profession = StringField("Profession", [DataRequired(), Length(max=30, min=2)])
    power = TextAreaField("Is power important to you? Defining goal: social status and prestige, control or dominance over people and resources.", [DataRequired(), Length(max=200)])