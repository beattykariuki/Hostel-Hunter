from flask_wtf import FlaskForm
from wtforms import Form,StringField,SelectField
from wtforms.validators import Required

class SearchForm(FlaskForm):
    choices=[('University','University'),
             ('Hostel','Hostel')]
    select = SelectField('search name....',choices=choices)

    search = StringField('')
    