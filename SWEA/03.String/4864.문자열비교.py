for tc in range(1, int(input())+1):
    pattern = list(input())
    string = list(input())
    # 완전탐색
    res = 0
    i, j = 0, 0
    while i < len(pattern) and j < len(string):
        if string[j] == pattern[i]:
            i += 1
            j += 1
        else:
            i = 0
            j += 1
    if i == len(pattern):
        res = 1
    else:
        res = 0
    print('#{} {}'.format(tc, res))
