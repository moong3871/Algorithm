def width(i, j):
    cnt = 1
    while j < n:
        j += 1
        if storage[i][j+1]:
            cnt += 1
        else:
            break
    return cnt


def height(i, j):
    cnt = 1
    while j < n:
        j += 1
        if storage[i+1][j]:
            cnt += 1
        else:
            break
    return cnt


def reset(ws, hs, w, h):
    for i in range(ws, w):
        for j in range(hs, h):
            storage[i][j] = 0
    return storage


for tc in range(1, int(input())+1):
    n = int(input())
    storage = list(list(map(int, input().split())) for _ in range(n))
    target_list = []
    for i in range(n):
        for j in range(n):
            if storage[i][j]:
                w = width(i, j)
                h = height(i, j)
                target_list.append([w, h, w*h])
                storage = reset(i, j, i+w, j+h)
    res = sorted(target_list, key=lambda x: (i[2], i[0]))
    print('#{} {}'.format(tc, len(res)), end=' ')
    for i in res:
        print('{} {}'.format(i[0], i[1]), end=' ')
    print()
