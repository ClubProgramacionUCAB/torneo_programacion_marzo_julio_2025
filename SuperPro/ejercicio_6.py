def sol(arr):
    m = 0
    arr = [int(n) for n in arr]
    for i in range(len(arr)):
        for j in range(len(arr)):
            m = max(m, (j - i)*min(arr[i], arr[j]))
    return m


print(sol(input().split(',')))
