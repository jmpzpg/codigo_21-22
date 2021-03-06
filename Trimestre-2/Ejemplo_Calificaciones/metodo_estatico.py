class Calificaciones():
    def __init__(self, alumno_lista=[]) -> None:
        
        if alumno_lista:
            self.__nombre = alumno_lista[0]
            self.__notas = alumno_lista[1:]
            self.__calificacion = self.calcula_calificacion()
        else:
            self.__nombre = ''
            self.__notas = []
            self.__calificacion = ''
            

    def __str__(self) -> str:
        return f'Alumno: {self.__nombre} tiene la calificación: {self.calificacion}'
        

    def calcula_calificacion(self):
        salida = ''
        if self.__notas:
            nota_media = sum(self.__notas) / len(self.__notas)
            if 0 < nota_media < 4.9:
                salida = 'SUSPENSO'
            elif 5 <= nota_media < 5.5:
                salida = 'SUFICIENTE'
            elif 5.5 <= nota_media < 6.5:
                salida = 'BIEN'
            elif 6.5 <= nota_media < 8.5:
                salida = 'NOTABLE'
            elif 8.5 <= nota_media < 9.5:
                salida = 'SOBRESALIENTE'
            else:
                salida = 'EXCELENTE'
        else:
            salida = None
        return salida

    def set_alumno(self, alum):
        self.__nombre = alum[0]
        for elem in alum[1:]:
            self.__notas.append(elem)
        self.__calificacion = self.calcula_calificacion()
    
    @property
    def alumno(self):
        return self.__nombre
    @alumno.setter
    def alumno(self, nuevo_alum):
        self.__nombre = nuevo_alum

    @property
    def notas(self):
        return self.__notas
    @notas.setter
    def notas(self, nuevas_notas):
        if self.valida_notas(nuevas_notas):
            self.__notas = nuevas_notas
            self.__calificacion = self.calcula_calificacion()
        else:
            raise Exception('Notas no válidas')

    @property
    def calificacion(self):
        return self.__calificacion

    @staticmethod
    def valida_notas(lista_notas):
        # verdadero si son validas (float entre 0 y 10) y false si no lo son
        # Falso para tipo distinto a int o float o lista vacia
        valido = True
        if not lista_notas:
            valido = False
        else:
            for elem in lista_notas:
                if not type(elem) in (int,float) or not 0.0 <= elem <= 10.0:
                    valido = False
        return valido


    # Añadido en clase del lunes 31-01-22 para el ejemplo de tener los alumnos con sus nots en un CSV
    @classmethod
    def alumnos_desde_csv():
        with open('archivo.csv', 'r') as manejador:
            filas = manejador.readline()
            for elem in filas:
                