from app.db import db

class Sede(db.Model):
    id_sede= db.Column(db.Integer, primary_key= True)
    id_empresa= db.Column(db.Integer, db.ForeignKey('empresa.id_empresa', ondelete='CASCADE'), nullable= False)
    id_departamento= db.Column(db.Integer, db.ForeignKey('departamento.id_departamento', ondelete='CASCADE'), nullable= False)