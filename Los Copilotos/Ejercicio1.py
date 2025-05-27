def romanToNumber(numeroRomano):
    romanDict = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

    acum=0
    for i in range(len(numeroRomano)-1): 
        if (romanDict.get(numeroRomano[i])>=romanDict.get(numeroRomano[i+1])):
            acum = acum + romanDict.get(numeroRomano[i])
        else:
            acum = acum - romanDict.get(numeroRomano[i])
    acum = acum + romanDict.get(numeroRomano[-1])
    return acum
        
print(romanToNumber("MCMXCIV"))
