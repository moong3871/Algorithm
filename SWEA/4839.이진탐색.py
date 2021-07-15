# 10개 중 1개의 오답으로 인해 오래 걸린 문제
# 책이 홀수이면 l = 1, 짝수이면 l = 0을 해줬던게 문제
# 엣지 케이스는 10 3 2
def search(entire, target):
    l = 1
    r = middle = entire
    cnt = 0
    while True:
        middle = (l + r) // 2
        if target > middle:
            l = middle
            cnt += 1
        elif target < middle:
            r = middle
            cnt += 1
        elif target == middle:
            break
        else:
            cnt = 0
            break
    return cnt


for tc in range(1, int(input()) + 1):
    P, Pa, Pb = map(int, input().split())
    if Pa == Pb:
        print('#{} {}'.format(tc, 0))
        break
    if search(P, Pa) > search(P, Pb):
        print('#{} {}'.format(tc, 'B'))
    elif search(P, Pa) < search(P, Pb):
        print('#{} {}'.format(tc, 'A'))
    else:
        print('#{} {}'.format(tc, 0))
