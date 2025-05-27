def dvide(listas):
    listanueva=[]
    if listas!=[]:
        for lista in listas:
            for item in lista:
                listanueva.append(item)
    return sorted(listanueva)

listas=[[1,4,5],[1,3,4],[2,6]]
print(dvide(listas))
