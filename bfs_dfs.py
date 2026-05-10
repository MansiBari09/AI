from collections import deque


class GraphTraversal:

    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = []

        for i in range(vertices):
            self.adjList.append([])

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    # DFS Recursive
    def dfsRecursive(self, node, visited):
        visited[node] = True

        print(node, end=" ")

        for neighbor in self.adjList[node]:
            if not visited[neighbor]:
                self.dfsRecursive(neighbor, visited)

    # BFS Recursive
    def bfsRecursive(self, queue, visited):

        if len(queue) == 0:
            return

        node = queue.popleft()
        print(node, end=" ")

        for neighbor in self.adjList[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

        self.bfsRecursive(queue, visited)


# ---------------- MAIN PROGRAM ----------------

vertices = int(input("Enter number of vertices: "))

graph = GraphTraversal(vertices)

while True:

    print("\n", "-" * 10, "MAIN MENU", "-" * 10)
    print("1. Add Edge")
    print("2. DFS Traversal")
    print("3. BFS Traversal")
    print("4. Display Graph")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        total = int(input("Enter total edges: "))

        for i in range(total):
            print(f"\nEdge {i + 1}")
            u = int(input("Enter first vertex: "))
            v = int(input("Enter second vertex: "))

            graph.addEdge(u, v)

    elif choice == 2:

        start = int(input("Enter starting vertex for DFS: "))

        visited = [False] * vertices

        print("DFS Traversal:")
        graph.dfsRecursive(start, visited)
        print()

    elif choice == 3:

        start = int(input("Enter starting vertex for BFS: "))

        visited = [False] * vertices

        queue = deque()

        visited[start] = True
        queue.append(start)

        print("BFS Traversal:")
        graph.bfsRecursive(queue, visited)
        print()

    elif choice == 4:

        print("\nAdjacency List:")

        for i in range(vertices):
            print(i, "->", graph.adjList[i])

    elif choice == 5:

        print("\nEND OF PROGRAM")
        break

    else:
        print("Invalid Choice")



#         Microsoft Windows [Version 10.0.22631.6199]
# (c) Microsoft Corporation. All rights reserved.

# C:\Users\mansi>python -u "e:\6_Sem\AI\AI\bfs_dfs.py"
# Enter number of vertices: 7

#  ---------- MAIN MENU ----------
# 1. Add Edge
# 2. DFS Traversal
# 3. BFS Traversal
# 4. Display Graph
# 5. Exit
# Enter your choice: 1
# Enter total edges: 6

# Edge 1
# Enter first vertex: 0
# Enter second vertex: 1

# Edge 2
# Enter first vertex: 1
# Enter second vertex: 3

# Edge 3
# Enter first vertex: 1
# Enter second vertex: 2

# Edge 4
# Enter first vertex: 0
# Enter second vertex: 4

# Edge 5
# Enter first vertex: 4
# Enter second vertex: 5

# Edge 6
# Enter first vertex: 5
# Enter second vertex: 6

#  ---------- MAIN MENU ----------
# 1. Add Edge
# 2. DFS Traversal
# 3. BFS Traversal
# 4. Display Graph
# 5. Exit
# Enter your choice: 2
# Enter starting vertex for DFS: 0
# DFS Traversal:
# 0 1 3 2 4 5 6 

#  ---------- MAIN MENU ----------
# 1. Add Edge
# 2. DFS Traversal
# 3. BFS Traversal
# 4. Display Graph
# 5. Exit
# Enter your choice: 3
# Enter starting vertex for BFS: 0
# BFS Traversal:
# 0 1 4 3 2 5 6 

#  ---------- MAIN MENU ----------
# 1. Add Edge
# 2. DFS Traversal
# 3. BFS Traversal
# 4. Display Graph
# 5. Exit
# Enter your choice: 4

# Adjacency List:
# 0 -> [1, 4]
# 1 -> [0, 3, 2]
# 2 -> [1]
# 3 -> [1]
# 4 -> [0, 5]
# 5 -> [4, 6]
# 6 -> [5]

#  ---------- MAIN MENU ----------
# 1. Add Edge
# 2. DFS Traversal
# 3. BFS Traversal
# 4. Display Graph
# 5. Exit
# Enter your choice: 5

# END OF PROGRAM
