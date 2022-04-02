def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    check = len(list(set(lottos) & set(win_nums)))
    zero = lottos.count(0)

    answer = [rank[zero + check], rank[check]]
    return answer
