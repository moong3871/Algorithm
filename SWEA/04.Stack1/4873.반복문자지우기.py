# stack 리스트의 마지막 문자와 비교 -> 반복이면 pop, 아니면 push
import sys
sys.stdin = open("input.txt", "r")
for tc in range(1, int(input())+1):
    texts = input()
    s = [texts[0]]
    for i in range(1, len(texts)):
        try:
            if s[-1] == texts[i]:
                s.pop(-1)
            else:
                s.append(texts[i])
        except IndexError:
            s.append(texts[i])
    print('#{} {}'.format(tc, len(s)))
