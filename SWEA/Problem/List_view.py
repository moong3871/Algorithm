import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    res = 0
    maxNum = 0
    for i in range(2, N-2):
        temp = buildings[i-2:i+3]
        if temp[2] != max(temp):
            continue
        else:
            maxNum = temp[2]
            temp.pop(2)
            res += maxNum - max(temp)
    print('#{} {}'.format(tc, res))
