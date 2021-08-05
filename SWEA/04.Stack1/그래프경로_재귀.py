import sys
sys.stdin = open("input.txt", "r")


def dfs(cur_node, end_node):
    global res
    if cur_node == end_node:
        res = 1
        return
    visited[cur_node] = 1
    for i in range(1, V+1):
        if arr[cur_node][i] == 1 and visited[i] == 0:
            dfs(i, end_node)
    return


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        st, ed = map(int, input().split())
        arr[st][ed] = 1
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    stack = []
    res = 0
    dfs(S, G)
    print('#{} {}'.format(tc, res))
