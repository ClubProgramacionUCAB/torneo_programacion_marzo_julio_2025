lista = [2,2,6,3,3,1,7,7,1]

def funcion(list):
    for i in range(0, len(list), 1):
        sum = 0
        for numero in list:
            if numero == list[i]:
                sum += 1
        if sum == 1:
            return list[i]
    return -1

print(funcion(lista))