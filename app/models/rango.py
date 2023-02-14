from app.db import db

class Rango(db.Model):
    id_rango= db.Column(db.Integer, primary_key=True)
    rango_velocidad= db.Column(db.String(50), nullable=False)
    rango_empresas= db.relationship('Rangoempresa', backref='rango', lazy=True)