import sys
sys.stdin = open("input.txt", "r")


def dfs(start, end):
    visit = []
    s = []
    s.append(start)

    while len(s) > 0:
        tmp = s.pop(-1)
        if tmp == end:
            return 1
        if tmp not in visit:
            visit.append(tmp)
            s.extend(w[tmp])  # tmp node의 인접노드를 stack에 추가
    return 0


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    w = [[] for _ in range(V+1)]
    for i in range(E):
        s, g = map(int, input().split())
        w[s].append(g)
    print(w)
    S, G = map(int, input().split())
    print('#{} {}'.format(tc, dfs(S, G)))
