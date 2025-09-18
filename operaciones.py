def funcionSuma(lista):
    suma = 0
    for num in lista:
        suma = suma +num
    return suma
print(funcionSuma([5,5,2,2,1]))


def funcionSumaMedia(lista):
    suma = 0
    for num in lista:
        suma = suma + num
    return suma,suma/len(lista)
tupla = funcionSumaMedia
print(tupla)