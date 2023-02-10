# separador = ","
# with open("data_internet.csv", encoding="utf-8") as archivo:
#         next(archivo)
#         listarucempresa= []
#         listanombrempresa= []
#         listaestadosunat= []
#         listadepartamento= []
#         listasegmento= []
#         listatecnologia= []
#         listarangovelocidad= []
#         for linea in archivo:
#             linea= linea.rstrip("\n")
#             columnas= linea.split(separador)
#             rucEmpresa= columnas[0]
#             nombreEmpresa= columnas[1]
#             estadoSunat= columnas[2]
#             departamento= columnas[3]
#             segmento= columnas[4]
#             tecnologia= columnas[5]
#             rango_velocidad= columnas[6]


def obtenerCsvComoDiccionarios(data_internet):
    separador = ","
    with open(data_internet, encoding="utf-8") as archivo:
        next(archivo)
        listas= []

        for linea in archivo:
            linea = linea.rstrip("\n")
            columnas = linea.split(separador)
            rucEmpresa= columnas[0]
            nombreEmpresa= columnas[1]
            estadoSunat= columnas[2]
            departamento= columnas[3]
            segmento= columnas[4]
            tecnologia= columnas[5]
            rango_velocidad= columnas[6]
            listas.append({
                "ruc_empresa": rucEmpresa,
                "nombre_empresa": nombreEmpresa,
                "estado_sunat": estadoSunat,
                "departamento": departamento,
                "segmento": segmento,
                "tecnologia": tecnologia,
                "rango_velocidad": rango_velocidad
            })
        # return (len(listas))
        return listas

# print(obtenerCsvComoDiccionarios("data_internet.csv"))

def principal():
    listas= obtenerCsvComoDiccionarios("data_internet.csv")
    lista_filtrados= []
    for lista in listas:
        if lista not in lista_filtrados:
            lista_filtrados.append(lista)
    print(lista_filtrados)
    print(len(lista_filtrados))
principal()