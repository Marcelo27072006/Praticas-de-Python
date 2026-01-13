tabela = sorted([0,1,2,3,4,4,5,5,6,8])

n = len(tabela)

q1 = tabela[:n//2]
q3 = tabela[n//2:]

def mediana(lista):
    m = len(lista)//2
    return lista[m]

Q1 = mediana(q1)

Q3 = mediana(q3)

IQR = Q3 - Q1

IQR_inf = Q1-(1.5*IQR)
IQR_sup = Q3+(1.5*IQR)

print(Q1)
print(Q3)
print("IQR:", IQR)
print("Limite inferior:", IQR_inf)
print("Limite superior:", IQR_sup)