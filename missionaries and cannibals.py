from collections import deque

def is_safe(m, c):
    return m == 0 or m >= c

def valid(state):
    m1, c1, boat, m2, c2 = state
    return (0 <= m1 <= 3 and 0 <= c1 <= 3 and
            0 <= m2 <= 3 and 0 <= c2 <= 3 and
            is_safe(m1, c1) and is_safe(m2, c2))

def successors(state):
    m1, c1, boat, m2, c2 = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    result = []
    for m, c in moves:
        if boat == 'L':
            new = (m1 - m, c1 - c, 'R', m2 + m, c2 + c)
        else:
            new = (m1 + m, c1 + c, 'L', m2 - m, c2 - c)
        if valid(new): result.append(new)
    return result

def bfs():
    start = (3, 3, 'L', 0, 0)
    goal = (0, 0, 'R', 3, 3)
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal:
            for p in path: print(p)
            return
        if state in visited: continue
        visited.add(state)
        for succ in successors(state):
            queue.append((succ, path + [succ]))

bfs()
