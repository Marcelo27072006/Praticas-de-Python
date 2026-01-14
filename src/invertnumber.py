l1 = [1, 3, 6]
l2 = [8, 5, 2]

def switch(lista):
    n = len(lista)
    i = 0
    j = n-1

    while i < j:
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1
        print(lista)
        return lista

switch(l1)
switch(l2)

