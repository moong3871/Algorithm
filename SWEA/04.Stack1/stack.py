# 스택 구현
# 구현한 스택으로 3개의 데이터 저장, 꺼내서 출력
def stack_push(a):
    s.append(a)
    return s


def stack_pop():
    if len(s) == 0:
        return False
    else:
        s.pop(-1)  # 가장 마지막 값을 뺀 s를 return
        return s


s = []
s = stack_push(2)
s = stack_push(3)
s = stack_push(1)
print(s)
s = stack_pop()
print('1번째 push {}'.format(s))
s = stack_pop()
print('2번째 push {}'.format(s))
s = stack_pop()
print('3번째 push {}'.format(s))
