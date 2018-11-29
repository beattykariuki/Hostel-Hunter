<<<<<<< HEAD
<<<<<<< HEAD
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [REquired()])
    submit = SubmitField('submit')
=======
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title = StringField('Review title', validators = [Required()])
    review = TextAreaField('Hostel review')
    submit = SubmitField('Submit')
>>>>>>> review
=======
from flask_wtf import FlaskForm
from wtforms import Form,StringField,SelectField
from wtforms.validators import Required

class SearchForm(FlaskForm):
    choices=[('University','University'),
             ('Hostel','Hostel')]
    select = SelectField('search name....',choices=choices)

    search = StringField('')
    
>>>>>>> searchHostel
