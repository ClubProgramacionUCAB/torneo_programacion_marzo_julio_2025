cd = str (input ("Ingrese el número romano: ")) + " "
sumt = 0
sumi = 0
i = 0
while (i <= len (cd) - 1):
    if (cd [i] == "I"):
        sumi += 1
        if (cd [i + 1] == "V" or cd [i + 1] == "X"):
            i += 1
            if cd [i] == "V":
                sumi = 5 - sumi
            else:
                sumi = 10 - sumi
        sumt += sumi
    elif (cd [i] == "V"):
        sumt += 5
    elif (cd [i] == "X"):
        sumi += 10
        if (cd [i + 1] == "L" or cd [i + 1] == "C"):
            i += 1
            if cd [i] == "L":
                sumi = 50 - sumi
            else:
                sumi = 100 - sumi
        sumt += sumi
    elif (cd [i] == "L"):
        sumt += 50
    elif (cd [i] == "C"):
        sumi += 100
        if (cd [i + 1] == "D" or cd [i + 1] == "M"):
            i += 1
            if cd [i] == "D":
                sumi = 500 - sumi
            else:
                sumi = 1000 - sumi
        sumt += sumi
    elif (cd [i] == "M"):
        sumt += 1000
    i+=1
    sumi = 0
print (sumt)