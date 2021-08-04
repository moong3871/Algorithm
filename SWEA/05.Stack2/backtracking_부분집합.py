def backtracking(index, letters):
    if index == len(li):
        res.append("".join(letters))
        return
    text = li[index]
    backtracking(index + 1, letters + [text])
    backtracking(index + 1, letters)


li = ['a', 'b', 'c']
res = []
backtracking(0, [])
print(res)
