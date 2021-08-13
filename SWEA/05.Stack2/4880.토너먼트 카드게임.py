def game(st_idx, ed_idx):
    if st_idx == ed_idx:
        return st_idx
    idx_1 = game(st_idx, (st_idx + ed_idx)//2)
    idx_2 = game((st_idx + ed_idx)//2 + 1, ed_idx)
    if (cards[idx_1] == 1 and cards[idx_2] == 2) or (cards[idx_1] == 2 and cards[idx_2] == 3) or (cards[idx_1] == 3 and cards[idx_2] == 1):
        return idx_2
    else:
        return idx_1


for tc in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, game(0, N-1) + 1))
