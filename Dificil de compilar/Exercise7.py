class Solution:
    def Exercise(array):
        list=[]
        for i in range(0,len(array)):
            list += array[i]
        print(list.count(1))

        longitud = len(list)

        for i in range(0, len(list), 1):
            for j in range(0, len(list),1):
                if (list[i] < list[j]):
                    remember = list[i]
                    list[i] = list[j]
                    list[j] = remember

        print(list)


Solution.Exercise([[1,3,4],[2,0,8]])