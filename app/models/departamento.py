from app.db import db

class Departamento(db.Model):
    id_departamento= db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50), nullable= False)
    sedes= db.relationship('Sede', backref='departamento', lazy=True)