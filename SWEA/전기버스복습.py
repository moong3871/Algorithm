for tc in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    battery = list(map(int, input().split()))
    bus_stop = [0]*N
    for i in range(M):
        bus_stop[battery[i]] = 1
    bus = K
    cnt = 0
    bus_stop[0] = -1
    while bus < N:
        # K칸 만큼 갔을 떄 충전기 있는지 확인
        if bus_stop[bus] == 1:
            bus_stop[bus] = -1
            cnt += 1
            bus += K
        elif bus_stop[bus] == 0:
            bus -= 1
        elif bus_stop[bus] == -1:
            cnt = 0
            break
    print('#{} {}'.format(tc, cnt))
