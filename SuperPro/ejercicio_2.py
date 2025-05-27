def reverse(x):
    negative = False
    if x < 0:
        negative = True

    res = str(abs(x))[::-1]
    while (res[0] == '0'):
        res = res[1::]

    num = (("-" if negative else "") + res)

    if -pow(2, 31) >= int(num) or int(num) >= pow(2, 31) - 1:
        return 0
    return num


print(reverse(int(input())))
