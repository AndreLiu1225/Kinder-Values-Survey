from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class MCQ(FlaskForm):
    age = IntegerField("Age", [DataRequired()])
    profession = StringField("Profession", [DataRequired(), Length(max=30, min=2)])

    power = RadioField("Defining goal: social status and prestige, control or dominance over people and resources."
                        ,choices=[('Yes','I want to be dominant'), ('No', 'Dominance over others is not the main priority')])

    tradition = RadioField("Defining goal: respect, commitment, and acceptance of the customs and ideas that one’s culture or religion provides."
                            ,choices=[('Yes', 'I would contribute to the survival and uniqueness of traditon'), ('No', 'I am always open and ready to change')])
    
    achievement = RadioField("Defining goal: personal success through demonstrating competence according to social standards."
                              ,choices=[('Yes', "I want to demonstrate competence in prevailing cultural standards and obtain social approval.'), ('No', 'I may want to achieve excellence, but it doesn't need to be socially approved")])
    
    stimulation = RadioField("Defining goal: excitement, novelty, and challenge in life."
                              ,choices=[('Yes', 'I want a challenging and exciting life.'), ('No', 'I prefer a life with lower amounts of stress.')])

    self_direction = RadioField("Defining goal: independent thought and action–choosing, creating, exploring."
                                 ,choices=[('Yes', 'I like freedom in thought and expression.'), ('No', 'Nah')])

    hedonism = RadioField("Defining goal: pleasure or sensuous gratification for oneself."
                          ,choices=[('Yes', 'My pleasure and satisfaction are of utmost priority'), ('No', 'Welfare of others is also important.')])
    
    conformity = RadioField("Defining goal: restraint of actions, inclinations, and impulses likely to upset or harm others and violate social expectations or norms."
                            ,choices=[('Yes', 'I do care about how others view me and follow the social norms'), ('No', 'I will do anything without a care.')])

    submit = SubmitField("Submit my answers.")

@app.route('/MCQ', methods=['POST','GET'])
def MCQ():
    form = MCQ()
    if form.validate_on_submit():
        return render_template('MCQ.html')

    

