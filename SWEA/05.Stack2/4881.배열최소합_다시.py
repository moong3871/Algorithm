#
def backtracking(idx, numbers):
    global sum_num, N
    if idx == N:
        print(numbers)
        if sum(numbers) < sum_num:
            sum_num = sum(numbers)
        return
    if sum(numbers) > sum_num:
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(i+1, numbers + [arr[idx][i]])
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sum_num = 9999999
    backtracking(0, [])
    print('#{} {}'.format(tc, sum_num))
