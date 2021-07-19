import sys
sys.stdin = open('sample_input.txt', "r")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    board = list(input() for _ in range(N))

    res = []
    for i in range(N):
        for start in range(N-M+1):
            if (board[i][start:start+M] == board[i][start:start+M][::-1]):
                res.append(''.join(board[i][start:start+M]))
        for start in range(N-M+1):
            col = []
            for c in range(M):
                col.append(board[start+c][i])
            if col[:] == col[::-1]:
                res.append(''.join(col[:]))
    print('#{} {}'.format(tc, res[0]))
