'''  Jose Manuel Perez Puig
Clase para modelar un aula y llevar los alumnos y sus notas'''

from genericpath import exists
from os import path
from claseAlumno import Alumno

class Curso():
    def __init__(self, nom_curso, listado_alumnos=[]) -> None:
        '''constructor de la clase. Recibe el nom_curso de la clase/aula
         y opcionalmente un listado de objetos Alumno'''
        self.__nombre_curso = nom_curso
        if listado_alumnos:
            self.__alumnos = listado_alumnos
        else:
            self.__alumnos = []


    @property
    def nombre_curso(self):
        return self.__nombre_curso

    @nombre_curso.setter
    def nombre_curso(self, nuevo_nombre):
        self.__nombre_curso = nuevo_nombre

    @property
    def alumnos(self):
        if self.__alumnos:
            salida = ''
            for elem in self.__alumnos:
                salida += f'{elem.nom_alumno} = {elem.notas_alumno}\n'
        else:
            salida = self.__alumnos
        return salida
    
    
    @property
    def listar_alumnos(self):
        '''lista los nombres de los alumnos actualmente en el curso'''
        salida = f'\n* * * Alumnos del curso de {self.__nombre_curso} * * *\n      -------\n'
        if self.__alumnos:
            for alum in self.__alumnos:
                salida += '       ' + alum.nom_alumno +'\n'
        else:
            salida = f'\n* * * El curso de {self.__nombre_curso} aun no tiene alumnos dados de alta * * *\n'
        return salida


    @property
    def listar_alumnos_y_notas(self):
        '''lista los nombres de los alumnos del curso con sus notas parciales'''
        salida = f'\n* * * Alumnos del curso de {self.__nombre_curso} con sus notas parciales * * *\n      -------\n'
        if self.__alumnos:
            for alum in self.__alumnos:
                n = self.__relleno(alum)
                salida += '       ' + alum.nom_alumno + n + ''.join(str(alum.notas_alumno)) + '\n'
        else:
            salida = f'\n* * * El curso de {self.__nombre_curso} aun no tiene alumnos dados de alta * * *\n'
        return salida



    def add_alumno(self, obj_alum):
        '''a??ade un nuevo objeto Alumno a la clase, que es pasado como par??metro'''
        if type(obj_alum) is Alumno:
            self.__alumnos.append(obj_alum)
        else:
            raise Exception('Error: Se esperaba una instancia de Alumno.')



    @classmethod
    def desde_csv(cls, nom_curso, archivo):
        '''m??todo factor??a para crear instancias de la clase Curso desde un archivo CSV'''
        lista_de_obj_alumnos = []

        try:
            with open(archivo, 'r') as manejador:
                filas = manejador.readlines()
                for fila_de_alumno in filas:
                    alum = []
                    lista_nombre_y_notas = fila_de_alumno[0:-1].split(',')
                    alum.append(lista_nombre_y_notas[0])
                    for nota in lista_nombre_y_notas[1:]:
                        if '.' in nota:
                            alum.append(float(nota))
                        else:
                            alum.append(int(nota))
                    obj_alum = Alumno(alum) 
                    lista_de_obj_alumnos.append(obj_alum)
        except FileNotFoundError:
                print('Error al abrir el archivo. Verifique la ruta del mismo')
        except ValueError:
                print('Error: El fichero contine alguna nota NO v??lida')
        except:
                print('Error inesperado abriendo el archivo')
        else:
            return cls(nom_curso, lista_de_obj_alumnos)


    def __max_long_nombres(self):
        max = 0
        for elem in self.__alumnos:
            longitud = len(elem.nom_alumno)
            if longitud > max:
                max = longitud
        return max + 2

    def __relleno(self, alumno):
        total = self.__max_long_nombres()
        salida = ' '
        for elem in range(total - len(alumno.nom_alumno)):
            salida += '-'
        salida += '> '
        return salida


    def __str__(self) -> str:
        salida = f'_______________________________________\nCurso de {self.__nombre_curso} - Alumnos y calificaciones:\n---------------------------------------\n'
        for alum in self.__alumnos:
            n = self.__relleno(alum)
            salida += '    '+ alum.nom_alumno + n + alum.calificacion + '\n'
        return salida


# ===============================================

curso = 'DAM'
archivo = '/Users/jmpp/Documents/GitHub/codigo_21-22/Trimestre-2/B03_Ejercicios_Calificaciones-CD_Libros/archivo_alumnos.csv'

a1 = Alumno(['Marcos', 5, 6, 7, 8, 9, 10])
a2 = Alumno(['Gabriel', 5, 6, 5, 6.5, 7, 6])
c = Curso(curso)
print(c.nombre_curso)
print(c.alumnos)

#clase2 = Curso('DAM')
#print(clase2.listar_alumnos)
#clase = Curso.desde_csv(curso, archivo)
#print(clase)
#alumno_nuevo = Alumno(['Juan Mar??a', 5, 6, 7, 8, 9, 10])
#clase.add_alumno(alumno_nuevo)
#print(clase)
#print(clase.alumnos_del_curso)
#print(clase.alumnos_y_notas)
""" 
Paco, 5, 6, 7, 8, 9, 8, 7.5
Antonio, 5, 6, 7, 7.5, 8, 9, 10
Mar??a, 5, 5, 5, 5, 5, 5, 5
 """