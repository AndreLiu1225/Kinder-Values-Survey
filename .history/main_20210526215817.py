from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "0c8973c8a5e001bb0c816a7b56c84f3a"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

db = SQLAlchemy(app)

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    profession = db.Column(db.String, nullable=False)
    power = db.Column(db.Integer, nullable=False)
    tradition = db.Column(db.Integer, nullable=False)
    achievement = db.Column(db.Integer, nullable=False)
    stimulation = db.Column(db.Integer, nullable=False)
    hedonism = db.Column(db.Integer, nullable=False)
    conformity = db.Column(db.Integer, nullable=False)
    self_direction = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Survey('{self.age}', '{self.name}', '{self.date_posted}')"


class MCQ(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    age = IntegerField("Please enter your age", validators=[DataRequired()])
    profession = StringField("What is your profession?", validators=[DataRequired(), Length(max=30)])
    power = IntegerField("Do you desire a higher social status and dominance over others? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)")
    tradition = IntegerField("Do you care about preserving traditions? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)")
    achievement = IntegerField("Is achievement according to social standards important? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)")
    stimulation = IntegerField("Do you prefer novel and exciting challenges in life? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)")
    hedonism = IntegerField("Is personal gratification the most important? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)")
    conformity = IntegerField("Do you think restraint of actions against social norms is important? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)")
    self_direction = IntegerField("Do you think independent thought and action are important (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)")
    submit = SubmitField("Submit")

@app.route('/', methods=['POST', 'GET'])
def values_quiz():
    form = MCQ()
    if form.validate_on_submit():
        post = Survey(age=form.age.data, name=form.name.data, profession=form.profession.data, power=form.power.data,
                      tradition=form.tradition.data, achievement=form.achievement.data, stimulation=form.stimulation.data,
                      hedonism=form.hedonism.data, conformity=form.conformity.data, self_direction=form.self_direction.data,)
        db.session.add(post)
        db.session.commit()
        flash(f'Survey is completed by {form.name.data}', 'success')
        return redirect(url_for('data_dashboard'))
    return render_template('MCQ.html', form=form)

@app.route('/results', methods=['GET', 'POST'])
def data_dashboard():
    return render_template('data_dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)

