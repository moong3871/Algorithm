# 0 = 통로, 1 = 벽, 2 = 출발, 3 = 도착
dr = [-1, 0, 0, 1]  # 상 우 하 좌
dc = [0, 1, -1, 0]  # 상 우 하 좌


def check(st):
    global res
    sr, sc = st
    visited[sr][sc] = 1
    for mode in range(4):
        nr = sr + dr[mode]
        nc = sc + dc[mode]
        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        if maze[nr][nc] == '3':
            res = 1
            return
        if maze[nr][nc] != '1' and visited[nr][nc] != 1:
            visited[nr][nc] = 1
            check((nr, nc))


for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    res = 0
    for i in range(N-1, 0, -1):
        if '2' in maze[i]:
            start = (i, maze[i].index('2'))
    check(start)
    print('#{} {}'.format(tc, res))
