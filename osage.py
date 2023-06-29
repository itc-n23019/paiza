def f(n, m, time):
    total_time = 0
    count = sum((total_time := total_time + t) <= n * 60 for t in time)
    return "OK" if count == m else str(count)

n = int(input())
m = int(input())
time = [int(input()) for _ in range(m)]

print(f(n, m, time))
