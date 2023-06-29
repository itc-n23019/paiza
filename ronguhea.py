def f(n):
    result = "lucky" if n % 7 == 0 else "unlucky"
    return result

n = int(input())
print(f(n))
