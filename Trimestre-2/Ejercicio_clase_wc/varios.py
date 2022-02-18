from unicodedata import normalize

def __gestionar_archivo(archivo):
        textchars = ''.join(map(chr, [7,8,9,10,12,13,27] + range(0x20, 0x100)))
        is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
        try:
            with open(archivo, 'r') as manejador:
                texto = manejador.readlines()
                if not is_binary_string(texto):
                    print('el archivo NO es binario')
        except Exception as e:
            print(type(e))
            print('ERROR: el archivo pasado es un ficero binario y no se puede analizar. Por favor, elija un fichero de texto')
            

def es_binario(archivo):
    lista_palabras = []
    ocurrencias = {}
    basura = ',;.:-_"?¿¡!'
    vocales_acentuadas = {'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
    contador_palabras = contador_lineas = 0
    try:
        with open(archivo, "r") as manejador:
            for linea in manejador:
                contador_lineas += 1
                linea_limpia = ''
                l = linea.lower()
                if l.endswith(' \n'):
                    l = l[0:-2]
                elif l.endswith(' '):
                    l = l[0:-1]
                for c in l:
                    if not c in basura and not c in vocales_acentuadas:
                        linea_limpia += c
                    elif c in vocales_acentuadas:
                        linea_limpia += vocales_acentuadas[c]
                lista_palabras = linea_limpia.split(' ')
                for palabra in lista_palabras:
                    contador_palabras += 1
                    if palabra in ocurrencias:
                        ocurrencias[palabra] += 1
                    else:
                        ocurrencias[palabra] = 1
        return [contador_lineas, contador_palabras, ocurrencias]
    except UnicodeDecodeError as e:
        print('ERROR: el archivo pasado NO es un ficero de texto y no se puede analizar. Por favor, elija un fichero de texto')
        


archivo= 'fichero.txt'

#s = 'Pingüino: Málaga es una ciudad fantástica y en Logroño me pica el... moño'
#s2 = normalize("NFKD", s).encode("ascii","ignore").decode("ascii")
#s1 = s.replace("ñ", "#").replace("Ñ", "%")
#s2 = normalize("NFKD", s1).encode("ascii","ignore").decode("ascii").replace("#", "ñ").replace("%", "Ñ")
#print(s)
#print(s2)

print(es_binario(archivo))
#__gestionar_archivo(archivo)