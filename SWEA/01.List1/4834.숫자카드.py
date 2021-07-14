# 똑같은 숫자가 여러개 일 수 O
# 최대최소 차이가 9
# -> 카운팅 정렬
for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input()))
    counts = [0] * (max(cards)+1)
    for card in cards:
        counts[card] += 1
    max_freq = max(counts)
    for i in range(len(counts)-1, -1, -1):
        if counts[i] == max_freq:
            print('#{} {} {}'.format(tc, i, max_freq))
            break
