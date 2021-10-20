nota = 10.5

if  nota < 0 or nota > 10:
    print("La nota no esta comprendida entre 0 y 10")

if 9<= nota <= 10:
    print('Sobresaliente')
elif 7<= nota <9:
    print('Notable')
elif 6 <= nota < 7:
    print('Bien')
elif 5 <= nota < 6 :
    print('Aprobado')
elif nota < 5 :
    print('Suspenso')
