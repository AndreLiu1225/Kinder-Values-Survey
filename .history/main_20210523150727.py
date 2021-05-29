from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = "0c8973c8a5e001bb0c816a7b56c84f3a"


class SimpleForm(FlaskForm):
    example = RadioField('Label', choices=[('value','description'),('value_two','whatever')])


@app.route('/',methods=['post','get'])
def hello_world():
    form = SimpleForm()
    if form.validate_on_submit():
        print(form.example.data)
    else:
        print(form.errors)
    return render_template('MCQ.html',form=form)




if __name__ == "__main__":
    app.run(debug=True)

