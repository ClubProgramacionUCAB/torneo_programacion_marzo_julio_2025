lista = [2,2,1,1,5,4,4]

def funcion(list):
    for i in range(0, len(list), 1):
        sum = 0
        for numero in list:
            if numero == list[i]:
                sum += 1
        if sum == 1:
            return list[i]
        
print(funcion(lista))