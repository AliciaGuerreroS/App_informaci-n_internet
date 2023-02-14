from app.db import db

class Empresa(db.Model):
    id_empresa= db.Column(db.Integer, primary_key= True)
    ruc= db.Column(db.String(20), nullable=False)
    nombre= db.Column(db.String(50), nullable= False)
    estado= db.Column(db.String(50), nullable= False)
    id_segmento= db.Column(db.Integer, db.ForeignKey('alcance.id_segmento', ondelete= 'CASCADE'), nullable=False)
    sedes= db.relationship('Sede', backref='empresa', lazy=True)
    rango_empresas= db.relationship('Rangoempresa', backref='empresa', lazy=True)

    def __init__(self, nombre, estado, id_segmento):
        self.nombre= nombre
        self.estado= estado
        self.id_segmento= id_segmento

        