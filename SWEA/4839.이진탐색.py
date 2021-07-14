for tc in range(1, int(input())+1):
    P, Pa, Pb = map(int, input().split())
    a, b, c = 0, 0, 0
    l, r = 0, P
    c = (l + r) // 2
    while c != Pa:
        print(c)
        if c < Pa:
            l = c
            print('l={}, c={}'.format(l, c))
            print(type(l), type(c))
            a += 1
        elif c < Pa:
            r = c
            a += 1
        elif c == Pa:
            break
        c = (l + r) // 2

        print(l, r, l + r - 1)
    l, r = 0, P
    c = (l + r) // 2
    while c != Pb:
        if c < Pb:
            l = c
            b += 1
        elif c < Pb:
            r = c
            b += 1
        elif c == Pb:
            break
        c = (l + r) // 2
    if a > b:
        print('#{} {}'.format(tc, 'B'))
    elif a < b:
        print('#{} {}'.format(tc, 'A'))
    else:
        print('#{} {}'.format(tc, 0))
