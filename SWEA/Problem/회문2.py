import sys
sys.stdin = open('input.txt', 'r')


def check(li):
    for i in range(len(li)//2):
        if li[i] != li[len(li)-i-1]:
            return False
    return True


for tc in range(1, 11):
    input()
    board = [input() for _ in range(100)]
    board2 = list(zip(*board))
    max_len = 1
    # 길이 100부터 -1 하면서 / 시작점 이동해가며/ 최대길이 구하기
    for length in range(100, 0, -1):
        for start in range(100-length+1):
            if max_len >= length:
                break
            for garo, sero in zip(board, board2):
                if check(garo[start:start+length]) or check(sero[start:start+length]):
                    max_len = length
                    break
    print('#{} {}'.format(tc, max_len))
