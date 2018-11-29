from flask_wtf import FlaskForm
from wtforms import Form,StringField,SelectField
from wtforms.validators import Required

class SearchForm(FlaskForm):
    choices=[('select','select'),
             ('University','University'),
             ('Hostel','Hostel')]
    select = SelectField('',choices=choices)

    search = StringField('')
    