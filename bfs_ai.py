def breadth_first_search(graph, start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)
        node = path[-1]
        if node in explored:
            continue
        explored.add(node)
        for next in graph.get(node, []):
            if next == goal:
                return path + [next]
            else:
                frontier.append(path + [next])
    return None 


graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

print(breadth_first_search(graph, 'A', 'F'))    
# create test cases for bfs ai  