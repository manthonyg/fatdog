from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fatdogdb.sqlite3'
db = SQLAlchemy(app)
db.create_all()
db.Model.metadata.reflect(db.engine)


class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return 'username:{}-password:{}'.format(self.username, self.password)


class Dogs(db.Model):
    __tablename__ = 'dogs'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.String(255))
    breed = db.Column(db.String(255))
    shape = db.Column(db.Integer)
    activity = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, age, breed, shape, activity, weight, user_id):
        self.name = name
        self.age = age
        self.breed = breed
        self.shape = shape
        self.activity = activity
        self.weight = weight
        self.user_id = user_id

    def __repr__(self):
        return 'name:{}-age:{}-breed:{}-shape:{}-activity:{}-weight:{}-user_id:{}'.format(self.name, self.age, self.breed, self.shape, self.activity, self.weight, self.user_id)


class Results(db.Model):
    __tablename__ = 'results'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    KGS = db.Column(db.Integer)
    RER = db.Column(db.Integer)
    MER = db.Column(db.Integer)
    suggested_calories = db.Column(db.Integer)
    dog = db.relationship(Dogs, backref='dog')

    def __init__(self, dog_id, user_id, KGS, RER, MER, suggested_calories):
        self.dog_id = dog_id
        self.user_id = user_id
        self.KGS = KGS
        self.RER = RER
        self.MER = MER
        self.suggested_calories = suggested_calories

    def __repr__(self):
        return 'suggested_calories{}-KGS:{}-RER:{}-MER:{}-DOG_ID{}'.format(self.suggested_calories, self.KGS, self.RER, self.MER, self.dog_id)