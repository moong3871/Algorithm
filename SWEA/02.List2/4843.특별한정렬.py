# 짝수 -> 최대값 / 홀수 -> 최소값 정렬
for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(10):
        for j in range(i+1, N):
            idx = i
            if i % 2 == 0:
                if numbers[idx] < numbers[j]:
                    idx = j
                    numbers[i], numbers[idx] = numbers[idx], numbers[i]
            else:
                if numbers[idx] > numbers[j]:
                    idx = j
                    numbers[i], numbers[idx] = numbers[idx], numbers[i]
    print('#{}'.format(tc), end=" ")
    print(*numbers[:10], sep=' ')
