def f(n, p, m, q):
    result = n * p + ((n + m - 1) // m) * q
    return result
    
n, p = map(int, input().split())
m, q = map(int, input().split())

print(f(n, p, m, q))
