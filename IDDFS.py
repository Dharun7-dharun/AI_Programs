def dls(graph, node, goal, depth, visited):
    if depth == 0 and node == goal:
        return True

    if depth > 0:
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dls(graph, neighbor, goal, depth - 1, visited):
                    return True
        visited.remove(node)

    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        print(f"\nSearching at depth {depth}...")
        if dls(graph, start, goal, depth, visited):
            print(f"✅ Goal '{goal}' found at depth {depth}")
            return
    print("Goal not found within depth limit")


graph = {}
n = int(input("Enter number of nodes: "))

print("Enter adjacency list (space-separated neighbors):")
for _ in range(n):
    node = input("Node: ")
    neighbors = input(f"Neighbors of {node}: ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

# Run IDDFS
iddfs(graph, start, goal, max_depth)