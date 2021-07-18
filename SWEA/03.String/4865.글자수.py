for tc in range(1, int(input())+1):
    pattern = input()
    string = input()
    cnt = [0]*len(pattern)
    for i in range(len(pattern)):
        for j in range(len(string)):
            if pattern[i] == string[j]:
                cnt[i] += 1
    print('#{} {}'.format(tc, max(cnt)))
