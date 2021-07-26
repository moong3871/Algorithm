import sys
sys.stdin = open("input.txt", "r")


def width(r, c):
    cnt = 0
    while arr[r][c]:
        cnt += 1
        c += 1
    return cnt


def height(r, c):
    cnt = 0
    while arr[r][c]:
        cnt += 1
        r += 1
    return cnt


def reset(r, c, x, y):
    for i in range(r, r+y):
        for j in range(c, c+x):
            arr[i][j] = 0
    return arr


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    matrix_list = []
    for r in range(n):
        for c in range(n):
            if arr[r][c]:
                x = width(r, c)
                y = height(r, c)
                arr = reset(r, c, x, y)
                matrix_list.append([y, x, x*y])
    res = sorted(matrix_list, key=lambda x: (x[2], x[0]))
    print('#{} {}'.format(tc, len(res)), end=' ')
    for r, c, size in res:
        print(c, r, end=' ')
    print()
