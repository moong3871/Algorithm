import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    sudoku = list(list(map(int, input().split())) for _ in range(9))
    res = 1
    for r in range(9):
        # 행 확인
        check = [0] * 10
        for c in range(9):
            check[sudoku[r][c]] += 1
        if max(check) > 1:
            res = 0
            break
    for r in [0, 3, 6]:
        check = [0] * 10
        for i in range(3):
            check[sudoku[r+i][i]] += 1
        if max(check) > 1:
            res = 0
            break
    for c in range(9):
        check = [0] * 10
        for i in range(9):
            check[sudoku[i][c]] += 1
        if max(check) > 1:
            res = 0
            break
    print('#{} {}'.format(tc, res))
