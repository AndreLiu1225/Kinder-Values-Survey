from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
import datetime
import plotly.graph_objs as go
import plotly.offline as plt

app = Flask(__name__)
app.config['SECRET_KEY'] = "0c8973c8a5e001bb0c816a7b56c84f3a"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

db = SQLAlchemy(app)

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    profession = db.Column(db.String(50), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    tradition = db.Column(db.Integer, nullable=False)
    achievement = db.Column(db.Integer, nullable=False)
    stimulation = db.Column(db.Integer, nullable=False)
    hedonism = db.Column(db.Integer, nullable=False)
    conformity = db.Column(db.Integer, nullable=False)
    security = db.Column(db.Integer, nullable=False)
    self_direction = db.Column(db.Integer, nullable=False)
    benevolence = db.Column(db.Integer, nullable=False)
    universalism = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Survey('{self.age}', '{self.name}', '{self.date_posted}')"

class MCQ(FlaskForm):
    email = StringField("What is your email?", validators=[DataRequired(), Email(message=('Not a valid email address')), Length(max=50)])
    age = IntegerField("Please enter your age", validators=[DataRequired()])
    profession = StringField("What is your profession?", validators=[DataRequired(), Length(max=30)])
    # Self-Enhancement
    power = IntegerField("Do you desire a higher social status and dominance over others? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])
    hedonism = IntegerField("Is personal gratification the most important? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])
    achievement = IntegerField("Is achievement according to social standards important? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])
    # Conservation
    tradition = IntegerField("Do you care about preserving traditions? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])
    conformity = IntegerField("Do you think restraint of actions against social norms is important? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])
    security = IntegerField("Do you value safety, harmony and stability of society, of relationships, and of self? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])
    # Openness to change
    stimulation = IntegerField("Do you prefer novel and exciting challenges in life? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])  
    self_direction = IntegerField("Do you think independent thought and action are important (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])
    # Self-transcendence
    benevolence = IntegerField("Are preserving and enhancing the welfare of your friends and family the most important? (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])
    universalism = IntegerField("I find it important to understand, tolerate, appreciate and protect all ethnicities and people. (4- It is my utmost priority, 3-It is important, 2-Doesn't bother me, 1-Not even a thought)", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=['POST','GET'])
def values_quiz():
    form = MCQ()
    if form.validate_on_submit():
        post = Survey(age=form.age.data, email=form.email.data, profession=form.profession.data, power=form.power.data,
                      tradition=form.tradition.data, achievement=form.achievement.data, stimulation=form.stimulation.data,
                      hedonism=form.hedonism.data, conformity=form.conformity.data, self_direction=form.self_direction.data,
                      benevolence=form.benevolence.data, universalism=form.universalism.data, security=form.security.data)
        # if Survey.is_email_in_database(form.email.data):
        #     flash(f"The user with {form.email.data} has already filled the survey", "danger")
        db.session.add(post)
        db.session.commit()
        flash(f'Survey is completed by {form.email.data}', 'success')
        power=form.power.data
        tradition=form.tradition.data
        achievement=form.achievement.data
        stimulation=form.stimulation.data
        hedonism=form.hedonism.data 
        conformity=form.conformity.data
        self_direction=form.self_direction.data
        benevolence=form.benevolence.data
        universalism=form.universalism.data
        security=form.security.data

        values = [power, tradition, achievement, stimulation, hedonism, conformity, security, self_direction, benevolence, universalism]
        values_labels = ['Openness to Change', 'Self-Transcendence', 'Conservation', 'Self-Enchancement']

        openness = [hedonism, stimulation, self_direction]
        self_enhancement = [hedonism, achievement, power]
        conservation = [tradition, conformity, security]
        self_trans = [universalism, benevolence]

        total_sum=sum(values)

        open_sum = round(sum(openness)/total_sum*100)
        enhance_sum = round(sum(self_enhancement)/total_sum*100)
        trans_sum = round(sum(self_trans)/total_sum*100)
        cons_sum = round(sum(conservation)/total_sum*100)

        sum_v = [open_sum, enhance_sum, trans_sum, cons_sum]

        trace1 = go.Bar(x=values_labels, y=sum_v)
        layout = go.Layout(title="")
        
        return render_template('data_dashboard.html', image=plt.show())
    else:
        flash('Ensure all questions are answered correctly', 'warning')
    return render_template('MCQ.html', form=form)

@app.route('/results', methods=['GET', 'POST'])
def data_dashboard():
    return render_template('data_dashboard.html', image=plt.show())

if __name__ == "__main__":
    app.run(debug=True)

