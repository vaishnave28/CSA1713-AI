def is_safe(state, node, color, graph):
    for neighbor in graph[node]:
        if state.get(neighbor) == color:
            return False
    return True

def map_coloring(graph, colors, state, nodes):
    if len(state) == len(nodes):
        return state
    node = [n for n in nodes if n not in state][0]
    for color in colors:
        if is_safe(state, node, color, graph):
            state[node] = color
            result = map_coloring(graph, colors, state, nodes)
            if result:
                return result
            del state[node]
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
solution = map_coloring(graph, colors, {}, list(graph.keys()))
print("Solution:", solution)
