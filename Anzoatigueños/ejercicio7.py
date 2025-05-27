listas = [[1, 4, 5], [1, 2, 4], [2, 6]]
lista = []
for lista_ in listas:
    for numero in lista_:
        lista.append(numero)

for i in range(0, len(lista) - 1, 1):
    for j in range (i+1, len(lista) - 1, 1):
        if lista[j] < lista[i]:
            aux = lista [j]
            lista [j] = lista [i]
            lista [i] = aux
            
print(lista)