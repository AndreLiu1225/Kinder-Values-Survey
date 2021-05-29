from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = "0c8973c8a5e001bb0c816a7b56c84f3a"

class MCQ(FlaskForm):
    age = IntegerField("Please enter your age", validators=[DataRequired()])
    profession = StringField("What is your profession?", validators=[DataRequired(), Length(max=30)])
    power = RadioField("Do you desire a higher social status and dominance over others?", choices=[('Yes', 'It is my priority'), ('No', 'It is not my priority')])
    tradition = RadioField("Do you care preserving traditions", choices=[('Yes', 'It is my priority'), ('No', 'It is not my priority')])
    achievement = RadioField("Is achievement according to social standards important?", choices=[('Yes', 'It is my priority'), ('No', 'It is not my priority')])
    stimulation = RadioField("Do you prefer novel and exciting challenges in life?", choices=[('Yes', 'It is my priority'), ('No', 'It is not my priority')])
    hedonism = RadioField("Do you desire a higher social status and dominance over others?", choices=[('Yes', 'It is my priority'), ('No', 'It is not my priority')])
    conformity = RadioField("Do you desire a higher social status and dominance over others?", choices=[('Yes', 'It is my priority'), ('No', 'It is not my priority')])
    self_direction = RadioField("Do you desire a higher social status and dominance over others?", choices=[('Yes', 'It is my priority'), ('No', 'It is not my priority')])
    submit = SubmitField("Submit")

if __name__ == "__main__":
    app.run(debug=True)

