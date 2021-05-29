from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

app = Flask(__name__)





if __name__ == "__main__":
    app.run(debug=True)

