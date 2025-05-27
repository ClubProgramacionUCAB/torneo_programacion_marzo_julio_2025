class Solution:
    def DivideTwoIntegers(dividendo, divisor):
        res = dividendo
        cont = 0
        hola = divisor
        if(divisor==0):
            print("error")
        else:
            if(divisor<0):
                divisor=divisor-divisor-divisor
            while(res >=divisor):
                cont = cont + 1
                res = res - divisor
            if (hola<0):
                cont=cont-cont-cont
            print(cont)

Solution.DivideTwoIntegers(7,-1)
