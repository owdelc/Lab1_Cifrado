def procesamiento(texto):
    textof = texto.upper()
    textof = textof.replace('Á','A')
    textof = textof.replace('É','E')
    textof = textof.replace('Í','I')
    textof = textof.replace('Ó','O')
    textof = textof.replace('Ú','U')

    exclusion = [' ',',', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')']
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
        file2.close

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
        file2.close
    
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
        file2.close

    return print('Cifrado realizado exitosamente!')
        



