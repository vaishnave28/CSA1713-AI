def alphabeta(depth, idx, is_max, values, alpha, beta):
    if depth == 3:
        return values[idx]
    if is_max:
        best = -999
        for i in range(2):
            val = alphabeta(depth+1, idx*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 999
        for i in range(2):
            val = alphabeta(depth+1, idx*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
result = alphabeta(0, 0, True, values, -999, 999)
print("Best value with Alpha-Beta Pruning:", result)
