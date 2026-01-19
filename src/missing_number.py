nums = [1, 2, 3, 4, 5, 6, 8, 9]

def miss(lista):
    j = 0
    for i in lista:
        j+=1
        if i != j:
            return j

contador = miss(nums)
print(contador)