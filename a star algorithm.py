from queue import PriorityQueue

def a_star(start, goal, graph, heuristic):
    open_set = PriorityQueue()
    open_set.put((heuristic[start], 0, start, [start]))  # (f, g, node, path)
    visited = set()

    while not open_set.empty():
        f, g, current, path = open_set.get()

        if current == goal:
            print("✅ Path found:", path)
            print("🧮 Total cost:", g)
            return

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                open_set.put((f_new, g_new, neighbor, path + [neighbor]))

    print("❌ No path found.")

# Sample Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('D', 1)],
    'D': [('F', 3)],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values (estimated cost to goal)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 2,
    'E': 1,
    'F': 0
}

# Run A* Search
a_star('A', 'F', graph, heuristic)
