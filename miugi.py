def f(n, m, s, t):
    c_count = {c: s.count(c) for c in set(s)}
    r_count = sum(1 if c_count.get(c, 0) == 0 or c_count[c] == 0 else c_count[c] - 1 for c in t)
    result = r_count
    return result
    
n, m = map(int, input().split())
s = input()
t = input()


print(f(n, m, s, t))
