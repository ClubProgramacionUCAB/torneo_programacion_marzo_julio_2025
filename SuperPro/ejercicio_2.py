def reverse(x):
    negative = False
    if x < 0:
        negative = True

    res = str(abs(x))[::-1]
    while (res[0] == '0'):
        res = res[1::]

    num = (("-" if negative else "") + res)

    if str(int(num)) != num:
        return 0
    return num


# El input aqui pls, no quiten int() :)
print(reverse(int(input())))
