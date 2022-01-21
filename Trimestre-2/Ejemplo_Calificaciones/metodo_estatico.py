class Calificaciones():
    def __init__(self, alumno_lista=[]) -> None:
        
        if alumno_lista:
            self.nombre = alumno_lista[0]
            self.notas = alumno_lista[1:]
            self.calificacion = self.calcula_calificacion()
        else:
            self.nombre = ''
            self.notas = []
            self.calificacion = ''
            

    def __str__(self) -> str:
        return f'Alumno: {self.nombre} tiene la calificación: {self.calificacion}'
        
        
    def calcula_calificacion(self):
        salida = ''
        if self.notas:
            nota_media = sum(self.notas) / len(self.notas)
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