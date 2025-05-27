dividendo = int (input())
divisor = int (input())
i = 0
suma = abs (dividendo)
while (suma - abs(divisor) > 0):
    suma -= abs(divisor)
    i += 1
if ((divisor > 0 and dividendo < 0) or (divisor < 0 and dividendo > 0)):
    print ("-", i)
else:
    print (i)
