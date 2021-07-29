# paper(n) = paper(n-1) + 2*paper(n-2)
# 10 <= N <= 300, N은 10의 배수
# n = N // 10

# naive
def paper_naive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper_naive(n-1) + 2*paper_naive(n-2)


# recursive_DP, top-down
arr = [0, 1, 3]


def paper_recur(n):
    if n < len(arr):
        return arr[n]
    else:
        paper = paper_recur(n-1) + 2*paper_recur(n-2)
        arr.append(paper)
        return paper

# recursive_DP, bottom-up


def paper_dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    arr = [0, 1, 3]
    for i in range(3, n+1):
        paper = arr[i-1] + 2*arr[i-2]
        arr.append(paper)
    return arr[n]
