# 왼쪽 괄호 -> push, 오른쪽 괄호 -> pop하여 짝인지 비교
# 디버깅하다보니 b가 '}'일 때, if b == '(' or '{' or '[' 을 통과하여 s에 추가되는 것을 발견했다.
# or 가 저렇게 쓰이면, b의 값을 확인하는 것이 아니라 b의 타입을 따지게 된다.
# 즉, 문자열 = 문자열 또는 문자열 또는 문자열인가? 라고 묻는 것이다.
# 따라서 true로 인식하고 if 조건문을 만족한 것이다.
bracket = ['(', ')', '{', '}', '[', ']']


def check(b):
    if b == '(' or b == '{' or b == '[':
        s.append(b)
        return 1
    else:
        if len(s) == 0:
            return 0
        tmp = s[-1]
        if bracket.index(b) == bracket.index(tmp) + 1:
            s.pop(-1)
            return 1
        else:
            return 0


for tc in range(1, int(input()) + 1):
    data = input()
    s = []
    res = 1
    for d in data:
        if d in bracket:
            res = check(d)
            if res == 0:
                res = 0
                break
    if len(s) > 0:
        res = 0

    print('#{} {}'.format(tc, res))
