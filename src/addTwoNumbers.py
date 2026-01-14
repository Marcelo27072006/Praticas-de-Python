l1 = [4, 8, 0, 7, 9, 0, 8]
l2 = [14, 6, 9]

def switch(lista):
    n = len(lista)
    inicio = 0
    fim = n-1
    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1
    print(lista)
    return lista

switch(l1)
switch(l2)

def breakdown(lista):
    contador = ""
    n = len(lista)
    for i in range(n):
        contador += str(lista[i])
    print(contador)
    return contador

resultado = int(breakdown(l1)) + int(breakdown(l2))
print(resultado)