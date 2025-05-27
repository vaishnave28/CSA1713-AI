def minimax(depth, is_max, values, idx):
    if depth == 3:
        return values[idx]
    if is_max:
        return max(minimax(depth+1, False, values, idx*2),
                   minimax(depth+1, False, values, idx*2+1))
    else:
        return min(minimax(depth+1, True, values, idx*2),
                   minimax(depth+1, True, values, idx*2+1))

# Game tree leaf values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Call minimax from root (depth=0, index=0, maximizing=True)
best_score = minimax(0, True, values, 0)
print("Best value for maximizer is:", best_score)
