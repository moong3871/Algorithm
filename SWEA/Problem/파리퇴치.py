import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    bugs = list(list(map(int, input().split())) for _ in range(N))
    dead_bugs_list = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            dead_bugs = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    dead_bugs += bugs[i][j]
            dead_bugs_list.append(dead_bugs)

    print('#{} {}'.format(tc, max(dead_bugs_list)))
