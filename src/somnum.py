def somnum(lista):
    for x in range(len(lista)):
        for y in range(len(lista)):
            soma = lista[x] + lista[y]
            if soma == target:
                return (lista[x], lista[y], soma)

target = int(input("Valor que quer alcançar: "))

nums = [2,7,11,15]

valor1, valor2, contador = somnum(nums)

print(f"Valor da soma de {valor1} + {valor2} é igual a {contador}")
