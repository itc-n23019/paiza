def f(a,  b):
    result = "ok" if b % a == 0 else "ng"
    return result
    
a, b =map(int,input().split())
print(f(a, b))
