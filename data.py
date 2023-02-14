import csv
def buscar_filtrado():
    with open("data_internet.csv", encoding= 'utf-8') as f:
        archivo= csv.reader(f)
        next(archivo)
        lista_elementos= []
        datos_filtrado= []

        for linea in archivo:
            elementos= linea[6]
            if elementos not in lista_elementos:
                lista_elementos.append(elementos)
                for i in lista_elementos:
                    if i == elementos:
                        datos_filtrado.append(linea)

        print(len(datos_filtrado))
        print(datos_filtrado[0])
        # print(lista_elementos)
buscar_filtrado()