for tc in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    battery = list(map(int, input().split()))
    stop = [0] * (N+1)
    for i in range(len(battery)):
        stop[battery[i]] = 1  # 충전기 위치 = 1
    cnt = 0  # 충전 횟수
    pos = K  # 버스 위치
    while pos < N:  # 정류장 내부에 버스가 있는 동안
        if stop[pos] == 1:  # 충전기가 있으면
            stop[pos] = -1  # 방문체크
            cnt += 1  # 이동수 체크
            pos += K  # 다음 칸으로 이동
        elif stop[pos] == 0:  # 충전기 없으면
            pos -= 1  # 한칸 뒤로 이동
        elif stop[pos] == -1:  # 이미 충전한 충전기이면
            cnt = 0
            break  # while문 빠져나가기
    print('#{} {}'.format(tc, cnt))
