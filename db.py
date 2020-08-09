from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)
db.create_all()
db.Model.metadata.reflect(db.engine)


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return 'username:{}-password:{}'.format(self.username, self.password)


class Dog(db.Model):
    __tablename__ = 'dogs'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(255))
    age = db.Column(db.String(255))
    breed = db.Column(db.String(255))
    shape = db.Column(db.Integer)
    activity = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    KGS = db.Column(db.Integer)
    RER = db.Column(db.Integer)
    MER = db.Column(db.Integer)
    breedStats = db.Column(db.String(100000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, age, breed, shape, activity, weight, KGS, RER, MER, breedStats, user_id):

        self.id = id
        self.name = name
        self.age = age
        self.breed = breed
        self.shape = shape
        self.activity = activity
        self.weight = weight
        self.KGS = KGS
        self.RER = RER
        self.MER = MER
        self.breedStats = breedStats
        self.user_id = user_id

    def __repr__(self):
        return 'name:{}-age:{}-breed:{}-shape:{}-activity:{}-weight:{}-KGS:{}-RER:{}-MER:{}-user_id:{}'.format(self.name, self.age, self.breed, self.shape, self.activity, self.weight, self.KGS, self.RER, self.MER, self.user_id)
