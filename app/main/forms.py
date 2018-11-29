class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [REquired()])
    submit = SubmitField('submit')