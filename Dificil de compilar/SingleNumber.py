
class Solution:
    def SingleNumber(lista):
        contApa = 1000000000000000000000000000000000000000000000000
        valor = 0
        list =[]
        list += lista
        for i in range (0,len(list),1):
            x = list[i]
            val = list.count(x)
            if(contApa>val):
                contApa=val
                valor = list[i]
        print(contApa)
        print(valor)

        


Solution.SingleNumber([8,8,8,9,0,0])    