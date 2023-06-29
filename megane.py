def f(N, num):
    mi = (N + 1) // 2 - 1
    result = num[mi]
    return result

N = int(input())
num = list(map(int, input().split()))
num.sort(reverse=True)
 
print(f(N, num))
