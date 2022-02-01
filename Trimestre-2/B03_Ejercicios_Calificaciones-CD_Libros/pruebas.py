def lista_de_alumnos_desde_csv(archivo):
    lista_de_alumnos = []
    with open(archivo, 'r') as manejador:
        filas = manejador.readlines()
        for fila_de_alumno in filas:
            alumno = []
            lista_nombre_y_notas = fila_de_alumno[0:-1].split(',')
            alumno.append(lista_nombre_y_notas[0])
            for nota in lista_nombre_y_notas[1:]:
                alumno.append(float(nota))
            lista_de_alumnos.append(alumno)
    return lista_de_alumnos


# =====================================
archivo = '/Users/jmpp/Documents/GitHub/codigo_21-22/Trimestre-2/B03_Ejercicios_Calificaciones-CD_Libros/archivo_alumnos.csv'
aula = lista_de_alumnos_desde_csv(archivo)
print(aula)
