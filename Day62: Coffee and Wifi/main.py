import os

from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os
from dotenv import load_dotenv

load_dotenv()

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["KEY"]
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    Location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    Open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    Close = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    Coffee = SelectField('Coffee Rating', choices=[('0','✘'),('1','☕'),('2','☕☕'),('3','☕☕☕'),('4','☕☕☕☕'),('5','☕☕☕☕☕')], validators=[DataRequired()])
    Wifi = SelectField('WiFi Strength Rating', choices=[('0','✘'),('1','💪'),('2','💪💪'),('3','💪💪💪'),('4','💪💪💪💪'),('5','💪💪💪💪💪')], validators=[DataRequired()])
    Power = SelectField('Power Socket Availability', choices=[('0','✘'),('1','🔌'),('2','🔌🔌'),('3','🔌🔌🔌'),('4','🔌🔌🔌🔌'),('5','🔌🔌🔌🔌🔌')], validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with (open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file):
            writer=csv.writer(csv_file)
            writer.writerow([
                form.cafe.data,
                form.Location.data,
                form.Open.data,
                form.Close.data,
                form.Coffee.data,
                form.Wifi.data,
                form.Power.data
            ])
        return redirect("/cafes")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
