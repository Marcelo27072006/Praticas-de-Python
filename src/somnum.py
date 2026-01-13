def soma():
    for i in nums:
        for y in nums[1:]:
            numero = i + y
            if numero == target:
                print(f"a soma de {i} + {y} + é igual a {target}")
                return

target = int(input("Valor que quer alcançar: "))
nums = [2,7,11,15]
soma()
