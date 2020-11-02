from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    title_blog = StringField('Title')
    description = TextAreaField('Description', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Comment')

class UpvoteForm(FlaskForm):
    submit = SubmitField('submit')

class DownvoteForm(FlaskForm):
    submit=SubmitField('submit')