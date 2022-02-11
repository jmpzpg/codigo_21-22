def is_anagram(cad1, cad2):

    if len(cad1) == len(cad2):
        salida = {l: cad1.count(l) for l in cad1} == {l: cad2.count(l) for l in cad2}
    else:
        salida = False
    return salida


print(is_anagram('typhoon', 'opython'))
print(is_anagram('Alice', 'Alici'))
print(is_anagram('Alice', 'Bob'))
print(is_anagram('test', 'tess'))