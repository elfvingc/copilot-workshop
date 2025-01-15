def depth_first_search(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            stack.extend(graph[vertex][::-1])

    return result


# Test the function
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
print("DFS traversal:", depth_first_search(graph, "A"))
print("Expected:      ['A', 'C', 'F', 'B', 'E', 'D']")
