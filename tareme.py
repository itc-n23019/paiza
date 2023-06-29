def f(s, n):
    result = "OK" if s >= n else "NG"
    return result

s, n = map(int, input().split())
print(f(s, n))
