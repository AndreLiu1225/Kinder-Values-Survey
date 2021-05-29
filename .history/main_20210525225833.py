from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = "0c8973c8a5e001bb0c816a7b56c84f3a"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

db = SQLAlchemy(app)

class Survey(db.Model):
    age = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)


class MCQ(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    age = IntegerField("Please enter your age", validators=[DataRequired()])
    profession = StringField("What is your profession?", validators=[DataRequired(), Length(max=30)])
    power = RadioField("Do you desire a higher social status and dominance over others?", choices=[(4, 'It is my utmost priority'), (3, 'It is my priority'), (2, 'Medium'), (1, 'It is not my priority')])
    tradition = RadioField("Do you care about preserving traditions", choices=[(4, 'It is my utmost priority'), (3, 'It is my priority'), (2, 'Medium'), (1, 'It is not my priority')])
    achievement = RadioField("Is achievement according to social standards important?", choices=[(4, 'It is my utmost priority'), (3, 'It is my priority'), (2, 'Medium'), (1, 'It is not my priority')])
    stimulation = RadioField("Do you prefer novel and exciting challenges in life?", choices=[(4, 'It is my utmost priority'), (3, 'It is my priority'), (2, 'Medium'), (1, 'It is not my priority')])
    conformity = RadioField("Do you think restraint of actions against social norms is important?", choices=[((4, 'It is my utmost priority'), (3, 'It is my priority'), (2, 'Medium'), (1, 'It is not my priority')])
    self_direction = RadioField("Do you think independent thought and action are important", choices=[(4, 'It is my utmost priority'), (3, 'It is my priority'), (2, 'Medium'), (1, 'It is not my priority')])
    submit = SubmitField("Submit")

@app.route('/', methods=['POST', 'GET'])
def values_quiz():
    form = MCQ()
    if form.validate_on_submit():
        print(form.example.data)
    else:
        print(form.errors)
    return render_template('MCQ.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)

