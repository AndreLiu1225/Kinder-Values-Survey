from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class MCQ(FlaskForm):
    age = IntegerField("Age", [DataRequired()])
    profession = StringField("Profession", [DataRequired(), Length(max=30, min=2)])

    power = SelectField("Defining goal: social status and prestige, control or dominance over people and resources."
                        ,choices=[('Yes','I want to be dominant'), ('No', 'Dominance over others is not the main priority')])

    tradition = SelectField("Defining goal: respect, commitment, and acceptance of the customs and ideas that one’s culture or religion provides."
                            ,choices=[('Yes', 'I would contribute to the survival and uniqueness of traditon'), ('No', 'I am always open and ready to change')])
    
    achievement = SelectField("Defining goal: personal success through demonstrating competence according to social standards."
                              ,choices=[('Yes', "I want to demonstrate competence in prevailing cultural standards and obtain social approval.'), ('No', 'I may want to achieve excellence, but it doesn't need to be socially approved")])
    
    stimulation = SelectField("Defining goal: excitement, novelty, and challenge in life."
                              ,choices=[('Yes', 'I want a challenging and exciting life.'), ('No', 'I prefer a life with lower amounts of stress.')])

    self_direction = SelectField("Defining goal: independent thought and action–choosing, creating, exploring."
                                 ,choices=[('Yes', )])

    

