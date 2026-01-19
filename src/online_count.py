grup = {"Alice": "online", "Bob": "offline", "Eve": "online"}

def online_count(lista):
    online = 0
    offline = 0
    for i in lista:
        if lista[i] == "online":
            online += 1
        else:
            offline += 1
    return {"online": online, "offline": offline}

contador = online_count(grup)

print(contador)
