from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class AddProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    skill = TextAreaField('Skill', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    url_tag = StringField('Alt tag', validators=[DataRequired()])