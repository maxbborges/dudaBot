#retorna uma string sem espaços e com a primeira letra de cada palavra maiuscula

def split_string(string):
    strArray = string.split()
    newString = ''
    for str in strArray:
        newString += str.title()
    return newString 