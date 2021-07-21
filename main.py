from cy import eceasar, deceasar, evigenere, devigenere, eafin, deafin, frecuencia, error 

'''
devigenere('text.txt', 'clave')

with open('text.txt', 'r') as file:
    data = file.read().replace('\n', '')

print (data)



def main():
    texto = 'TEXTOAFIN'
    llave = [17, 20]
 
    texto_encriptado = eafin(texto, llave)
 
    print('Texto encriptado: {}'.format( texto_encriptado ))
 
    print('Texto desencriptado: {}'.format
    ( deafin(texto_encriptado, llave) ))
 
 
if __name__ == '__main__':
    main()
'''
str = 'OSCAAAR'
error(str)