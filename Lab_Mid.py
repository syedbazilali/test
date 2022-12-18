graph = {
150: [2, 80],
5: [2, 45],
74: [80, 102],
165: [45, 102],
2: [150, 5, 145],
80: [150, 145, 74],
45: [5, 145, 165],
102: [74, 145, 165],
145: [2, 80, 45, 102]
}
visited = []
def dfs(visited, graph, node):
 if node not in visited:
  print(node)
 visited.append(node)
 for neighbour in graph[node]:
  dfs(visited, graph, neighbour)
print("Depth-First Search :")
dfs(visited, graph, 150)
