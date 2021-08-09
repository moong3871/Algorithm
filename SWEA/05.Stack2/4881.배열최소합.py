import sys
sys.stdin = open("input.txt", "r")


def backtracking(idx, numbers):
    global sum_num, N
    if idx == N:
        if numbers < sum_num:
            sum_num = numbers
        return
    if numbers > sum_num:
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            numbers += arr[idx][i]
            backtracking(idx+1, numbers)
            visited[i] = 0
            numbers -= arr[idx][i]


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sum_num = 9999
    backtracking(0, 0)
    print('#{} {}'.format(tc, sum_num))
