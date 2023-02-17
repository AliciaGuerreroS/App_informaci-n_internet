from app import create_app
from flask import Flask
from app.db import db
from flask_marshmallow import Marshmallow
from app.models.alcance import Alcance
from app.models.empresa import Empresa
from app.models.sede import Sede
from app.models.departamento import Departamento
from app.models.rango_empresa import Rangoempresa
from app.models.rango import Rango
from flask import render_template, request, jsonify


app=create_app()
ma= Marshmallow(app)
#######################
class AlcanceSchema(ma.Schema):
    class Meta:
        fields= ('id_segmento', 'nombre_segmento', 'nombre_tecnologia')
        model= Alcance

alcance_schema= AlcanceSchema()
alcance_schema= AlcanceSchema(many=True)

#######################
class EmpresaSchema(ma.Schema):
    class Meta:
        fields= ('id_empresa', 'ruc', 'nombre', 'estado', 'id_segmento')
        model= Empresa

empresa_schema= EmpresaSchema()
empresa_schema= EmpresaSchema(many=True)

#######################
class EmpresaSchema(ma.Schema):
    class Meta:
        fields= ('id_empresa', 'nombre', 'estado', 'id_segmento')
        model= Empresa

empresa_schema= EmpresaSchema()
empresa_schema= EmpresaSchema(many=True)

#######################
class SedeSchema(ma.Schema):
    class Meta:
        fields= ('id_sede', 'id_empresa', 'id_departamento')
        model= Sede

sede_schema= SedeSchema()
sede_schema= SedeSchema(many=True)

#######################
class DepartamentoSchema(ma.Schema):
    class Meta:
        fields= ('id_departamento', 'nombre')
        model= Departamento

departamento_schema= DepartamentoSchema()
departamento_schema= DepartamentoSchema(many=True)

#######################
class RangoempresaSchema(ma.Schema):
    class Meta:
        fields= ('id_rango_empresa', 'id_rango', 'id_empresa')
        model= Rangoempresa

rangoempresa_schema= RangoempresaSchema()
rangoempresa_schema= RangoempresaSchema(many=True)

######################
class RangoSchema(ma.Schema):
    class Meta:
        fields= ('id_rango', 'rango_velocidad', 'id_empresa')
        model= Rango

rango_schema= RangoSchema()
rango_schema= RangoSchema(many=True)


@app.route('/',methods=['GET']) #ruta raiz
def index():
    todas_empresas= Empresa.query.all()
    return render_template('inicio.html', todas_empresas= todas_empresas)

# @app.route('/verSede',methods=['GET']) 
# def ver_sede():

#     sede_depa= Departamento.query.all()
#     return render_template('versede.html', sedes = sede_depa)

###endpoint para ver las sedes que existen
@app.route("/sedes", methods=['GET'])
def ver_sedes():
    departamento= Departamento.query.all()
    resultado= departamento_schema.dump(departamento)
    return jsonify(resultado)

###endpoint para ver las empresas que se encuentran en cada departamento
@app.route("/empresa_departamento", methods=['GET'])
def ver_empresa_departamento():
    sedes= Sede.query.all()
    resultado= sede_schema.dump(sedes)
    return jsonify(resultado)

###endpoint para ver las empresas que existen
@app.route("/empresas", methods=['GET'])
def ver_empresas():
    empresas= Empresa.query.all()
    resultado= empresa_schema.dump(empresas)
    return jsonify(resultado)


db.init_app(app)
with app.app_context():
    db.create_all()
    print("Base de datos conectado!")



if __name__ == "__main__":
    app.run(debug=True)