from queue import PriorityQueue

def a_star(start, goal, graph, h):
    open_set = PriorityQueue()
    open_set.put((0 + h[start], 0, start, [start]))
    visited = set()

    while not open_set.empty():
        f, g, node, path = open_set.get()
        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                open_set.put((g + cost + h[neighbor], g + cost, neighbor, path + [neighbor]))

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 5)],
    'D': []
}
heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
a_star('A', 'D', graph, heuristic)
