
class Solution:
    def ReverseInteger(integer):
        numero = str(integer)
        respuesta = 0
        if (numero[0] == "-"):
            respuesta = numero[::-1]
            respuesta = "-"+respuesta[0:-1:]
        else:
            respuesta = numero[::-1]

        print(int(respuesta))
Solution.ReverseInteger(-10)
