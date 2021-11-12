"""
https://www.codewars.com/kata/565b9d6f8139573819000056

You have managed to intercept an important message and you are trying to read it.

You realise that the message has been encoded and can be decoded by switching each letter with a corresponding letter.

You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.

For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc

You read the first sentence:

"r slkv mlylwb wvxlwvh gsrh nvhhztv"

After a few minutes you manage to decode it:

"i hope nobody decodes this message"

Create a function that will instantly decode any of these messages

You can assume no punctuation or capitals, only lower case letters, but remember spaces!


assert_equals(decode("svool"),"hello")


def decode(message):
    #your code here

"""

def decode(message):
    listado_derecho = list('abcdefghijklmnopqrstuvwxyz')
    lista_cad_in = list(message)
    lista_salida = []
    for i in lista_cad_in:
        if i == ' ' or i == '.' or i == ',':
            lista_salida.append(i)
        else:
            indice_derecho = listado_derecho.index(i)
            indice_reves = 25 - indice_derecho
            lista_salida.append(listado_derecho[indice_reves])
    return ''.join (lista_salida)
    

print(decode('abc abc'))