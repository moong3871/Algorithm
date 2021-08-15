for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    while M:
        tmp = numbers.pop(0)
        numbers.append(tmp)
        M -= 1
    print('#{} {}'.format(tc, numbers[0]))
