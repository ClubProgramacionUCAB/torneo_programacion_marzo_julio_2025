class Solution:
    def RomanToInteger(cadena):
        respuesta = 0
        numerosRomanos = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(0,len(cadena),1):
            letra = cadena[i]
            vletra=numerosRomanos[letra]
            if (i != len(cadena)-1):
                sig= cadena[i+1]
                sletra = numerosRomanos[sig]
                if (vletra >= sletra):
                    respuesta += vletra
                else: 
                    respuesta -= vletra
            else:
                respuesta += vletra

        print(respuesta)
Solution.RomanToInteger("XLD")
