# 슬라이스의 idx가 음수이면, 빈 리스트가 출력된다
# arr = [0,1,2]
# arr[2:-1:-1] => [], arr[2::-1] => [0,1,2]
import sys
sys.stdin = open("sample_input.txt", "r")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    board = list(input() for _ in range(N))
    res = ''
    for i in range(N):
        if res != '':
            break
        for j in range(N-M+1):  # 가로 회문 탐색
            if j == 0:  # 슬라이싱에서 음수가 있으면 빈 배열 출력, 따라서 0인 경우와 그렇지 않은 경우 구분
                if board[i][j:j+M] == board[i][j + M - 1::-1]:
                    res = board[i][j:j+M]
                    print(j, j+M, board[i][j:j+M])
                    break
            elif board[i][j:j+M] == board[i][j + M - 1:j - 1:-1]:
                res = board[i][j:j+M]
                break
    if res == '':
        for r in range(N-M+1):
            for c in range(N):
                col = []
                for i in range(M):
                    col.append(board[r+i][c])
                if col[:] == col[::-1]:
                    res = ''.join(col)
                    break
    print('#{} {}'.format(tc, res))
