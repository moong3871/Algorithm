import sys
sys.stdin = open("input.txt", "r")
# arr = 간선이 존재하는 경우 1로 표기한 2차원 리스트


def dfs(cur_node, end_node):
    stack = []
    stack.append(cur_node)
    while stack:
        tmp = stack.pop()
        if tmp == end_node:
            return 1
        if visited[tmp] == 0:
            visited[tmp] = 1
            for i in range(1, V+1):
                if arr[tmp][i] == 1 and visited[i] == 0:
                    stack.append(i)
    return 0


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        st, ed = map(int, input().split())
        arr[st][ed] = 1
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    print('#{} {}'.format(tc, dfs(S, G)))
