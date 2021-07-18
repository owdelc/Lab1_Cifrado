from cy import eceasar, deceasar, evigenere



evigenere('text.txt', 'clave')

with open('text.txt', 'r') as file:
    data = file.read().replace('\n', '')

print (data)




