# A가 고정이므로 A의 모든 부분집합 구하기도 전역 가능
A = [i for i in range(1, 13)]
length = len(A)

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    cnt = 0
    # A의 부분집합 다 구하기
    for i in range(1 << length):  # A의 전체 부분집합 갯수
        parts = []
        for j in range(length):  # A 원소 수만큼 비트 비교
            if i & (1 << j):
                parts.append(A[j])
        if (len(parts) == N) & (sum(parts) == K):  # 조건 확인
            cnt += 1
    print('#{} {}'.format(tc, cnt))
