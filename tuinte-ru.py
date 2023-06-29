def f(s, t):
    p = "-" * s
    p = p[:t-1] + "+" + p[t:]
    return p
    
s = int(input())
t = int(input())

print(f(s, t))
