import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    case_no = input()
    arr = list(list(map(int, input().split())) for _ in range(100))
    sum_list = []
    # 각 행의 합과 최대값 비교
    for r in range(100):
        sum_list.append(sum(arr[r]))
    # 각 열의 합과 최대값 비교
    for c in range(100):
        col_sum = 0
        for r in range(100):
            col_sum += arr[r][c]
        sum_list.append(col_sum)
    # 대각선의 합과 최대값 비교
    diag_sum1, diag_sum2 = 0, 0
    for r in range(100):
        for c in range(100):
            if r == c:
                diag_sum1 += arr[r][c]
        diag_sum2 += arr[r][99-r]
        sum_list.append(diag_sum1)
        sum_list.append(diag_sum2)
    print('#{} {}'.format(tc, max(sum_list)))
