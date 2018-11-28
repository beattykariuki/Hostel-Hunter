from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class SearchForm(FlaskForm):
    name = StringField('University Name:', validators=[Required()])

    search = TextAreaField('search name....')

    submit = SubmitField('Submit')
  