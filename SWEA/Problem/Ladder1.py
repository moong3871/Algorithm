import sys
sys.stdin = open('input.txt', 'r')

dr = [0, 0, -1, 1]  # 좌, 우, 상, 하
dc = [-1, 1, 0, 0]


def dfs(tr, tc):
    res = -1
    stack = [[tr, tc]]
    while res == -1:
        cur = stack.pop()
        for mode in range(4):
            nr = cur[0] + dr[mode]
            nc = cur[1] + dc[mode]
            if nr < 0 or nr > 99 or nc < 0 or nc > 99:
                continue
            if ladder[nr][nc] == 1:
                if nr == 0:
                    res = nc
                    break
                stack.append([nr, nc])
                ladder[nr][nc] = 3
                break
    return res


for test_case in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(99, 0, -1):
        if int(2) in ladder[i]:
            tr, tc = i, ladder[i].index(2)
            break
    print('#{} {}'.format(test_case, dfs(tr, tc)))
