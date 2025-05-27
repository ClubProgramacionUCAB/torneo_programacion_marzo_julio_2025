def container(height):
    height = [int(n) for n in height]
    p1 = 0
    p2 = len(height) - 1

    res = 0

    for i in range(len(height)):
        res = max(res, (p2 - p1) * min(height[p1], height[p2]))
        if p1 > p2:
            break
        if height[p1] - height[p1 + 1] < height[p2] - height[p2 - 1]:
            p1 += 1
        else:
            p2 -= 1

    return res
    
print(container(input().split(',')))
