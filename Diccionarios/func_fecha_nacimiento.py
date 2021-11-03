fecha = input('Introduce tu fecha de nacimiento como DD/MM/AAAA: ')
lista = fecha.split('/')
lista_meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
print (f' - Naciste el dia {lista[0]} de {lista_meses[int(lista[1]) - 1]} del año {lista[2]}')
