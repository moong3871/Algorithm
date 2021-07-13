# 정렬 이론 공부 후 문제를 봤더니
# 오름차순으로 정렬한 채로 문제를 풀었다.
# 이 문제는 주어진 배열을 임의로 정렬하지 않는다(그런 조건 없음!!)
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    MAX = sum(num[:M])
    MIN = int(30000*100)
    for i in range(N-M+1):
        if sum(num[i:i+M]) > MAX:
            MAX = sum(num[i:i+M])
        elif sum(num[i:i+M]) < MIN:
            MIN = sum(num[i:i+M])
    print('#{} {}'.format(tc, MAX-MIN))
