class GraphColoring:

    def __init__(self, adjacencyMatrix, numColors):

        self.V = len(adjacencyMatrix)
        self.graph = adjacencyMatrix
        self.colors = [0] * self.V

        self.colorNames = ["", "Red", "Green", "Blue", "Yellow", "Orange"]

    # Check if color can be assigned
    def isSafe(self, v, c):

        for i in range(self.V):

            if self.graph[v][i] == 1 and self.colors[i] == c:
                return False

        return True

    # Recursive function
    def solveGraphColoring(self, v, m):

        if v == self.V:
            self.printSolution()
            return True

        for c in range(1, m + 1):

            if self.isSafe(v, c):

                self.colors[v] = c

                if self.solveGraphColoring(v + 1, m):
                    return True

                self.colors[v] = 0

        return False

    # Print solution
    def printSolution(self):

        print("\nVertex Colors:")

        for i in range(self.V):

            print(f"Vertex {i} -> {self.colorNames[self.colors[i]]}")

    # Start solving
    def solve(self, m):

        if not self.solveGraphColoring(0, m):

            print("No solution exists.")


# ---------------- USER INPUT ----------------

V = int(input("Enter number of vertices: "))

print("Enter adjacency matrix row by row:")

graph = []

for i in range(V):

    row = list(map(int, input(f"Row {i}: ").split()))

    graph.append(row)

numColors = int(input("Enter number of colors: "))

gc = GraphColoring(graph, numColors)

gc.solve(numColors)