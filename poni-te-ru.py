def check_str(str):
    count = sum(a == b for a, b in str)
    return "OK" if count >= 3 else "NG"

str = [input().split() for _ in range(5)]
result = check_str(str)
print(result)
