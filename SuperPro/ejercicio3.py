def single(nums):
    n = dict()
    for i in nums:
        if i not in n:
            n[i] = 0
        n[i] += 1

    for i in n.keys():
        if n[i] == 1:
            return i

    return 0


# poner el array donde dice input() :)
print(single(input()))
