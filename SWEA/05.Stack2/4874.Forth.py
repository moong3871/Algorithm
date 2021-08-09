import sys
sys.stdin = open("input.txt", "r")

operator = ['+', '-', '*', '/']


def cal(oper):
    if len(stack) < 2:
        return False
    try:
        tmp2, tmp1 = int(stack.pop()), int(stack.pop())
    except:
        return sys.float_repr_style
    if oper == '+':
        return tmp1 + tmp2
    elif oper == '-':
        return tmp1 - tmp2
    elif oper == '*':
        return tmp1 * tmp2
    elif oper == '/':
        return tmp1 // tmp2


for tc in range(1, int(input()) + 1):
    infos = input().split()
    stack = []
    for info in infos:
        if info == '.':
            if len(stack) > 1:
                res = 'error'
            else:
                res = stack.pop()
        elif info in operator:
            res = cal(info)
            if res:
                stack.append(res)
            else:
                res = 'error'
                break
        else:
            stack.append(info)
    print('#{} {}'.format(tc, res))
