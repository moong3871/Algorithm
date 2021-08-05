import sys
sys.stdin = open("input.txt", "r")
# 방향성 그래프
# adj = 인접노드가 담긴 2차원 리스트
# dfs, 필요한 것 = 인접행렬, 방문체크, 스택
# 스택에서 pop하고 -> 방문안했으면 방문체크 -> 인접행렬 있으면 스택에 추가


def dfs(cur_node, end_node):
    stack.append(cur_node)
    while stack:
        tmp = stack.pop()
        if tmp == end_node:
            return 1
        if visited[tmp] == 0:
            visited[tmp] = 1
            stack.extend(adj[tmp])
    return 0


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        st, ed = map(int, input().split())
        adj[st].append(ed)
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    stack = []
    print('#{} {}'.format(tc, dfs(S, G)))
