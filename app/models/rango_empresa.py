from app.db import db

class Rangoempresa(db.Model):
    id_rango_empresa= db.Column(db.Integer, primary_key=True)
    id_rango= db.Column(db.Integer, db.ForeignKey('rango.id_rango', ondelete='CASCADE'), nullable=False)
    id_empresa=db.Column(db.Integer, db.ForeignKey('empresa.id_empresa', ondelete='CASCADE'), nullable=False)
