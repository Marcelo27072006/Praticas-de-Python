nums = [1, 2, 3, 6, 7, 8, 9, 10]

def ultima_pagina(lista):
    contador = ""
    for i in range(len(lista)):

        no = lista[i]

        next_no = lista[(i+1)]

        contador += str(no)

        if no+1 != next_no:
            return contador

    contador += str(lista)
    return contador

contador = ultima_pagina(nums)
print(contador)
