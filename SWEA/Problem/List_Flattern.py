import sys
sys.stdin = open('input.txt', 'r')
# 가장 높은/낮은 블록을 찾는다.
# 해당 블록 -= 1, += 1, 덤프횟수차감
for tc in range(1, 11):
    dump = int(input())
    blocks = list(map(int, input().split()))
    high, low = 0, 0
    for _ in range(dump):
        # 가장 높/낮은 블록 찾기
        for i in range(100):
            if blocks[i] > blocks[high]:
                high = i
            elif blocks[i] < blocks[low]:
                low = i
            # dump 횟수 이내에 평탄화 완료 시
            # if blocks[high] == blocks[low]:
            #     break
        # dump
        blocks[high] -= 1
        blocks[low] += 1

    maxIdx, minIdx = 0, 0
    for i in range(100):
        if blocks[i] > blocks[maxIdx]:
            maxIdx = i
        elif blocks[i] < blocks[minIdx]:
            minIdx = i
    print('#{} {}'.format(tc, blocks[maxIdx] - blocks[minIdx]))
