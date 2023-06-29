def f(a, b):
    result = a - b if a > b else 0
    return result

a, b = map(int, input().split())

print(f(a, b))
