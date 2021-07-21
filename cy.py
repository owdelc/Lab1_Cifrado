import numpy as np
import nltk
from nltk.probability import FreqDist
import re


def procesamiento(texto):
    textof = texto.upper()
    textof = textof.replace('Á','A')
    textof = textof.replace('É','E')
    textof = textof.replace('Í','I')
    textof = textof.replace('Ó','O')
    textof = textof.replace('Ú','U')

    exclusion = [' ',',', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', '!', '¡', '?', '¿']
    for i in exclusion:
        textof = textof.replace(i, '')
    return textof


def eceasar(mensaje, llave):
    nuevo = ''
    with open(mensaje, 'r') as file:
        data = file.read().replace('\n', '')

    n_mensaje = procesamiento(data)

    control = ord('A')

    for i in n_mensaje:
        if i.isupper():
            #uni = ord(i)

            indice = ord(i) - control
        
            n_indice = (indice + llave) % 26

            n_uni = n_indice + control

            n_letra = chr(n_uni)

            nuevo = nuevo + n_letra

        else:
            i.upper()
            
            #uni = ord(i)

            indice = ord(i) - control
        
            n_indice = (indice + llave) % 27

            uni = n_indice + control

            n_letra = chr(uni)

            nuevo = nuevo + n_letra
    
    with open(mensaje, 'w') as file2:
        file2.write(nuevo)
        file2.close()

    return print('Cifrado realizado exitosamente!')
    
    
def deceasar(cifrado, llave):

    mensaje = ''

    with open(cifrado, 'r') as file:
        data = file.read().replace('\n', '')

    n_cifrado = procesamiento(data)

    control = ord('A')

    for i in n_cifrado:

        if i.isupper():  
            indice = ord(i) - control
            
            n_indice = (indice - llave) % 27

            uni = n_indice + control

            n_letra = chr(uni)

            mensaje = mensaje + n_letra
        
        else:

            i.upper()

            indice = ord(i) - control
            
            n_indice = (indice - llave) % 27

            uni = n_indice + control

            n_letra = chr(uni)

            mensaje = mensaje + n_letra

    with open(cifrado, 'w') as file2:
        file2.write(mensaje)
        file2.close()
    
    return print('Descifrado realizado exitosamente!')

            
def evigenere(mensaje, llave):
    base = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    actual = 0

    nuevo = ''

    with open(mensaje, 'r') as file:
        data = file.read().replace('\n', '')

    n_mensaje = procesamiento(data)

    for i in n_mensaje:
        if i.isupper():
            s = base.find(i) + base.find(llave[actual % len(llave)])
            m = int(s) % len(base)
            nuevo = nuevo + str(base[m])

            actual = actual + 1 

        else:
            i.upper()
            s = base.find(i) + base.find(llave[actual % len(llave)])
            m = int(s) % len(base)
            nuevo = nuevo + str(base[m])

            actual = actual + 1
    
    with open(mensaje, 'w') as file2:
        file2.write(nuevo)
        file2.close()

    return print('Cifrado realizado exitosamente!')
        

def devigenere(cifrado, llave):

    base ='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

    mensaje = ''

    actual = 0

    with open(cifrado, 'r') as file:
        data = file.read().replace('\n', '')

    n_cifrado = procesamiento(data)

    for i in n_cifrado:
        s = base.find(i) - base.find(llave[actual % len(llave)])
        m = int(s) % len(base)
        mensaje = mensaje + str(base[m])

        actual = actual + 1
    else:

        i.upper()

        s = base.find(i) - base.find(llave[actual % len(llave)])
        m = int(s) % len(base)
        mensaje = mensaje + str(base[m])

        actual = actual + 1


    with open(cifrado, 'w') as file2:
        file2.write(mensaje)
        file2.close()


def aeuclidiano(x, y):
    a,b, c,d = 0,1, 1,0
    while x != 0:
        e, f = y//x, y%x
        g, h = a-c*e, b-d*e
        y,x, a,b, c,d = x,f, c,d, g,h
    euclidiano = y
    return euclidiano, a, b
 
def moduloinverso(x, g):
    euclidiano, a, b = aeuclidiano(x, g)
    if euclidiano != 1:
        return None  
    else:
        return a % g
 

def eafin(texto, clave):

    return ''.join([ chr((( clave[0]*(ord(t) - ord('A')) + clave[1] ) % 27)
                  + ord('A')) for t in texto.upper().replace(' ', '') ])
 

def deafin(cifrado, clave):

    return ''.join([ chr((( moduloinverso(clave[0], 27)*(ord(c) - ord('A') - clave[1]))
                    % 27) + ord('A')) for c in cifrado ])
 

def frecuencia(mensaje):

    n_mensaje = procesamiento(mensaje)
    d = {}
    teorica = np.array([('A', 0.1253),('B', 0.0142), ('C', 0.0468), ('D', 0.0586),('E', 0.1368), ('F', 0.0069),('G', 0.0101), ('H', 0.007), ('I', 0.0625), ('J', 0.0044), ('K', 0.0002), ('L', 0.0497), ('M', 0.0315), ('N', 0.0671), ('Ñ', 0.0031), ('O', 0.0868), ('P', 0.0251), ('Q', 0.0088), ('R', 0.0687), ('S', 0.0798), ('T', 0.0463), ('U', 0.0393), ('V', 0.009), ('W', 0.0001), ('X', 0.0022), ('Y', 0.009), ('Z', 0.0052)])

    x = len(mensaje)

    ## Arreglar organizacion token 
    token = re.findall('.', n_mensaje)

    dist = nltk.FreqDist(token)

    d = dist.most_common(100000000000)

    array = [a[1] for a in d]
    f = np.array(array)

    array2= [a[1] for a in teorica]
    er = np.array(array)

    ## Arreglar probabilidad y error
    prob = f/f.sum()
    error = er-f

    print (token)
    print('Este es el error: ', error)
    print('Estas son las frecuencias: ', f)
    print('Esta es la probabilidad: ', prob)

def fuerza_ceasar(maximo, mensaje):
    for i in range(maximo):
        clave = deceasar(mensaje, i)
        frecuencia(clave)

        

    
""" mensaje = "mensaje"
    diccionario =  {}
    for char in set(a):
        d[char] = a.count(char)


"""




