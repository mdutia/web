from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
Bootstrap(app)

Criteria= ['Criterion 1','Criterion 2','Criterion 3','Criterion 4','Criterion 5' ]

from app import views

class User(db.Model):
    #__bind_key__='users'
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    pwd = db.Column(db.String(120), unique=False)
    firstname= db.Column(db.String(120), unique=False)
    lastname= db.Column(db.String(120), unique=False)
    matric= db.Column (db.String(20))    
    groupnumber= db.Column (db.Integer)
    status= db.Column (db.String(10))
#    data = db.Column(db.String(255))

    def __init__(self, username, pwd, fname, lname, matric, groupnumber, status):
        self.username = username
        self.pwd = pwd
        self.firstname= fname
        self.lastname= lname
        self.groupnumber= groupnumber
        self.matric= matric
        self.status= status

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % self.username

class Evaluation(db.Model):
    __bind_key__='evaluations'
    id = db.Column(db.Integer, primary_key=True)
    markee_matric = db.Column(db.String(20))
    marker_matric = db.Column(db.String(20))
    m1= db.Column (db.Integer)
    m2= db.Column (db.Integer)
    m3= db.Column (db.Integer)
    m4= db.Column (db.Integer)
    m5= db.Column (db.Integer)
    j1= db.Column (db.String (255))

    
    def __init__(self, markee, marker, m1,m2,m3,m4,m5,j1):
        self.markee_matric=markee
        self.marker_matric=marker
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
        self.j1=j1


    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % self.markee_matric
   

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))