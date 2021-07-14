for tc in range(1, int(input())+1):
    N = int(input())
    board = list([0] * 11 for _ in range(11))
    color = []
    cnt = 0
    for _ in range(N):
        x1, y1, x2, y2, value = map(int, input().split())
        # 색칠-처음이면 칠하고 / 같은 색이면 pass / 다른 색이면 plus
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if board[i][j] == 0:
                    board[i][j] = value
                elif board[i][j] == value:
                    continue
                else:
                    board[i][j] += value
                    if board[i][j] == 3:
                        cnt += 1

    print('#{} {}'.format(tc, cnt))
