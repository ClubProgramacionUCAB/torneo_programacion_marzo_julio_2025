numero = input()
cadena = ""
for i in range (len(numero)-1,-1, -1):
    cadena += numero[i]
    
print(int(cadena))