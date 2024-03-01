from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title',db.String())
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    description = db.Column('Description',db.Text())
    skill = db.Column('Skills Practiced',db.String())
    url = db.Column('URL',db.String())
    url_tag = db.Column('Alt tag',db.String())


    def __repr__(self):
        return f'''<Project (Title: {self.title}
        Created: {self.created}
        Description: {self.description}
        Skill: {self.skill}
        URL: {self.url}
        Alt tag: {self.url_tag}
        '''
