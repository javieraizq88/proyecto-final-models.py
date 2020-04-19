from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
#######
# Administrador
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=True)
    lastname = db.Column(db.String(100), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable = False)
    role = db.relationship(Role)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow )
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "lastname": self.lastname,
            "role": self.role.serialize(),
            "created": self.date_created,
        }
########
# CLIENTE
class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    planes_id = db.Column(db.Integer, db.ForeignKey('planes.id'), nullable=False)
    # username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # objective = db.Column(db.Text, nullable=True)
    objective = db.relationship('Objective', backref ='client_detail', lazy=True)
    # age = db.Column(db.Integer, nullable=True)
    photo = db.Column(db.String(100), nullable=False, default='default_profile.png')
    role = db.relationship(Role)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
##### formulario nutricionista ingreso cliente ######
    gemder = db.Column(db.String(100), nullable=True)
    nivelEducacional = db.Column(db.String(100), nullable=True)
    trabajo = db.Column(db.String(100), nullable=True)
    enfermedades = db.Column(db.String(100), nullable=True)
    orina = db.Column(db.String(100), nullable=True)
    digestion = db.Column(db.String(100), nullable=True)
##### formulario personal trainer ingreso cliente ######
    def serialize(self):
        return {
            "id": self.id,
            "planes_id": self.planes_id,
            "username": self.username,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "objecive": self.objecive,
            "age": self.age,
            "photo": self.photo,
            "role": self.role.serialize(),
            "created": self.date_created
            ##### formulario
        }
######
# PROFESIONALES (Personal trainer y nutricionista)
class Profesional(db.Model):
    __tablename__ = 'profesional'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    #planes_id = db.Column(db.Integer, db.ForeignKey('planes.id'), nullable=False)
    # username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(100), nullable=False, default='default_profile.png')
    specialties = db.Column(db.String(100), nullable=True)
    education = db.Column(db.String(100), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    lastWork = db.Column(db.String(100), nullable=True)
    lastWorkyears = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)
    role = db.relationship(Role)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow )
    auth = db.Column(db.Boolean, nullable = False, default = False)
    def serialize(self):
        return {
            "id": self.id,
            "role_id": self.role_id,
            #"planes_id": self.planes_id,
            # "username": self.username,
            "authorized":self.auth,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname,
            "photo": self.photo,
            "specialties": self.specialties,
            "education": self.education,
            "age": self.age,
            "lastWork": self.lastWork,
            "lastWorkyears": self.lastWorkyears,
            "description": self.description,
            "role": self.role.serialize(),
            "created": self.date_created
        }
####### CONVERSAR SI ESTO VA O NO
#  Plan de cada cliente q tiene nut y pt en cada plan para q quede como historial 
class Planes(db.Model):
    __tablename__ = 'planes'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    profesional_id = db.Column(db.Integer, db.ForeignKey('profesional.id'), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "profesional_id": self.profesional_id,
        }
class Objective(db.Model):
    __tablename__= 'objective'
    id = db.Column(db.Integer, primary_key=True)
    objective = db.Column(db.Text, nullable=False)
    observation = db.Column(db.Text, nullable = True)
    age = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable = False)

    def serialize(self):
        return {
            "id": self.id,
            "objective": self.objective,
            "observation": self.observation,
            "age": self.age,
            "date_created": self.date_created,
            "client_id": self.client_id,
        }