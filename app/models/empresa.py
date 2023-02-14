from app.db import db

class Empresa(db.Model):
    id_empresa= db.Column(db.Integer, primary_key= True)
    nombre= db.Column(db.String(50), nullable= False)
    estado= db.Column(db.String(50), nullable= False)
    id_segmento= db.Column(db.Integer, db.ForeignKey('segmento.id', ondelete= 'CASCADE'), nullable=False)

    def __init__(self, nombre, estado, id_segmento):
        self.nombre= nombre
        self.estado= estado
        self.id_segmento= id_segmento