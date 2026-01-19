nums = [5, 10, 20, 15, 30]

def max_min(lista):
    menor = lista[0]
    maior = lista[0]
    for i in lista:
        if i < menor:
            menor = i
        elif i > maior:
            maior = i
    output = maior - menor
    return output

contador = max_min(nums)
print(contador)