from genericpath import exists
from os import path
from claseAlumno import Alumno

class Aula():
    def __init__(self, nom, archivo) -> None:
        if self.__comprueba_archivo(archivo):
            self.__nombre_clase = nom
            self.__alumnos = []
            self.__carga_alumnos(archivo)
        else:
            raise FileNotFoundError('El archivo no existe o no se ha encontrado. Revise la ruta del archivo')

    def __comprueba_archivo(self, archivo):
        if path.exists(archivo):
            resp = True
        else:
            resp = False
        return resp
    
    def __carga_alumnos(self, archivo):
        listado = self.__lista_de_alumnos_desde_csv(archivo)
        for alum in listado:
            alumno = Alumno(alum)
            self.__alumnos.append(alumno)

    
    def __lista_de_alumnos_desde_csv(self, archivo):
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

    def __str__(self) -> str:
        salida = f'_______________________________________\nClase de {self.__nombre_clase} - Alumnos y calificaciones:\n---------------------------------------\n'
        for alum in self.__alumnos:
            salida += f'    {alum.nom_alumno} ---> {alum.calificacion}\n'
        return salida


# ===============================================
curso = 'DAM'
archivo = '/Users/jmpp/Documents/GitHub/codigo_21-22/Trimestre-2/B03_Ejercicios_Calificaciones-CD_Libros/archivo_alumnos.csv'
clase = Aula(curso, archivo)
print(clase)