from app.db import db

class Alcance(db.Model):
    id_segmento= db.Column(db.Integer, primary_key= True)
    nombre_segmento= db.Column(db.String(50), nullable= True)
    nombre_tecnologia= db.Column(db.String(50), nullable= True)
    empresas= db.relationship('Empresa', backref='alcance', lazy= True)

    def __init__(self, nombre_segmento, nombre_tecnologia):
        self.nombre_segmento= nombre_segmento
        self.nombre_tecnologia= nombre_tecnologia