from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields import DateField
from wtforms.validators import DataRequired, URL


class AddProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    skills = TextAreaField('Skills', validators=[DataRequired()], render_kw={"placeholder": "Enter skills here..."})
    url = StringField('URL', validators=[DataRequired(), URL()])
    url_tag = StringField('Project Name', validators=[DataRequired()])
    completion_date = DateField('Completion Date', format='%Y-%m', validators=[DataRequired()])
