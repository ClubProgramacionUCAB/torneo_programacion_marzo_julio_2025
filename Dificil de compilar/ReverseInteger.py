
class Solution:
    def ReverseInteger(integer):
        numero = str(integer)
        respuesta = ""
        signo = ""
        if (numero[0] == "-"):
            signo = "-"
            respuesta = numero[::-1]
            respuesta = respuesta[0:-1:]
        else:
            respuesta = numero[::-1]
        print(signo+respuesta)
Solution.ReverseInteger(23446858)