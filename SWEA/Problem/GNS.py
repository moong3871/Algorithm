import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    input()
    new_number = ['ZRO', 'ONE', 'TWO', 'THR',
                  'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    numbers = list(map(str, input().split()))
    check = [0]*10
    for number in numbers:
        check[new_number.index(number)] += 1
    print('#{}'.format(tc))
    for i in range(10):
        print('{} '.format(new_number[i])*check[i])
    # for idx, cnt in enumerate(check):
    #     print('{} '.format(new_number[idx])*cnt)
