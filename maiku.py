def f(a, b):
    result = b // (2 * a)
    result += 1 if b % (2 * a) != 0 else 0
    return result

a = int(input())
b = int(input())

print(f(a, b))
