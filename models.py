from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'project.db')
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    completion_date = db.Column('Completion Date', db.Date)  # Change here
    description = db.Column('Description', db.Text())
    skills = db.Column('Skills', db.Text())
    url = db.Column('URL', db.String())
    url_tag = db.Column('Alt tag', db.String())

    def __repr__(self):
        return f'''<Project (Title: {self.title}
        Completion Date: {self.completion_date}
        Description: {self.description}
        Skills: {self.skills}
        URL: {self.url}
        Alt tag: {self.url_tag}
        '''
