test_case = int(input())
for case in range(1, test_case+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # 방법1. 라이브러리 사용
    # max_num = max(numbers)
    # min_num = min(numbers)
    # print("#{} {}".format(case, max_num-min_num))

    # 방법2. 직접 비교
    max_num, min_num = 0, 1000000
    for number in numbers:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
    print("#{} {}".format(case, max_num-min_num))
