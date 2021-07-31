N = int(input())
if N == 1:
    res = 1
elif N == 2:
    res = 2
else:
    a, b = 1, 2
    for i in range(3, N+1):
        a, b = b, (a+b) % 15746
        res = b
print(res)
