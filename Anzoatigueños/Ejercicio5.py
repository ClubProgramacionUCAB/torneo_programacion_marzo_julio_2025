dividendo = int (input())
divisor = int (input())
if (divisor == 0):
    print("divisor no puede ser igual a 0")
else:
    i = 0
    suma = abs (dividendo)
    while (suma - abs(divisor) >= 0):
        suma -= abs(divisor)
        i += 1
    if ((divisor > 0 and dividendo < 0) or (divisor < 0 and dividendo > 0)):
        print (-i)
    else:
        print (i)