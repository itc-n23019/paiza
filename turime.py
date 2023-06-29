def f(p, point):
    point = p // 100 + 10 if p >= 1000 else p // 100
    return point

p = int(input())
point = p // 100 

print(f(p,point))
