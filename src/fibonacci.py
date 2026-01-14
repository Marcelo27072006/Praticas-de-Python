def fibonacci(valor):
    i = 0
    soma = 1
    while i <= valor:
        print(i)
        contador = soma
        soma = i
        i = contador + soma

fibonacci(valor = int(input("Digite um valor até o alcance da fórmula: ")))