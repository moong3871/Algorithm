# DP는 규칙을 만드는게 먼저!!
# 0과 1의 횟수도 피보나치 규칙과 같다.
# 단, 초기값이 다르므로 2차원 배열
arr = [[1, 0], [0, 1]]
for tc in range(1, int(input())+1):
    n = int(input())
    if n < len(arr):
        print('{} {}'.format(arr[n][0], arr[n][1]))
    else:
        for i in range(len(arr), n+1):
            arr_0 = arr[i-1][0] + arr[i-2][0]
            arr_1 = arr[i-1][1] + arr[i-2][1]
            arr.append([arr_0, arr_1])
        print('{} {}'.format(arr[n][0], arr[n][1]))
