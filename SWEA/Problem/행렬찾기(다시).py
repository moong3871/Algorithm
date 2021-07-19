# 각각의 가로, 세로가 다르다. (행, 렬의 개수가 서로 다르다)
# #tc 부분행렬 개수 행크기 열크기
# 크기(행X열) 작은순, 같은 크기이면 행이 작은 순
def width(i, j):
    cnt = 1
    dx = j
    while True:
        dx += 1
        if dx >= N:
            break
        if


for tc in range(1, int(input())+1):
    n = int(input())
    storage = list(list(map(int, input().split())) for _ in range(n))

    for i in range(n):
        for j in range(n):
            if storage[i][j]:
                w = width(i, j)
                h = height(i, j)
