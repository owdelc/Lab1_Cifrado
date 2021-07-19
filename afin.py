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
 

def main():
    texto = 'TEXTOAFIN'
    llave = [17, 20]
 
    texto_encriptado = eafin(texto, llave)
 
    print('Texto encriptado: {}'.format( texto_encriptado ))
 
    print('Texto desencriptado: {}'.format
    ( deafin(texto_encriptado, llave) ))
 
 
if __name__ == '__main__':
    main()
    