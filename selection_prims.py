
graph = []


# ---------------- PRIM'S MST ----------------

def prims_mst(graph):

    if not graph:
        print("Graph is empty. Please input graph first.")
        return

    n = len(graph)

    selected = [False] * n
    selected[0] = True

    no_of_edges = 0
    total_weight = 0

    print("\nEdge : Weight")

    while no_of_edges < n - 1:

        minimum = float('inf')
        x = -1
        y = -1

        for i in range(n):

            if selected[i]:

                for j in range(n):

                    if not selected[j] and graph[i][j] != 0:

                        if graph[i][j] < minimum:

                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y} : {graph[x][y]}")

        total_weight += graph[x][y]

        selected[y] = True

        no_of_edges += 1

    print("Total Minimum Weight:", total_weight)


def input_graph():

    graph.clear()

    V = int(input("Enter number of vertices: "))

    print("Enter adjacency matrix (use 0 if no edge):")

    for i in range(V):

        row = list(map(int, input(f"Row {i}: ").split()))

        graph.append(row)


# ---------------- SELECTION SORT ----------------

def selection_sort(arr):

    n = len(arr)

    print("\nPasses of Selection Sort:\n")

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"Pass {i + 1}: {arr}")

    return arr


def input_array():

    n = int(input("Enter number of elements: "))

    arr = []

    for i in range(n):

        value = int(input(f"Enter element {i + 1}: "))

        arr.append(value)

    selection_sort(arr)

    print("\nSorted Array:")

    for i in range(n):
        print(arr[i], end=" ")

    print()


# ---------------- MAIN MENU ----------------

def main():

    while True:

        print("\n", "-" * 10, "MAIN MENU", "-" * 10)

        print("1. Input Graph")
        print("2. Run Prim's MST Algorithm")
        print("3. Perform Selection Sort")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            input_graph()

        elif choice == 2:

            prims_mst(graph)

        elif choice == 3:

            input_array()

        elif choice == 4:

            print("Exiting Program...")
            break

        else:

            print("Invalid choice! Please try again.")


main()


# Microsoft Windows [Version 10.0.22631.6199]
# (c) Microsoft Corporation. All rights reserved.

# C:\Users\mansi>python -u "e:\6_Sem\AI\AI\selection_prims.py"

#  ---------- MAIN MENU ----------
# 1. Input Graph
# 2. Run Prim's MST Algorithm
# 3. Perform Selection Sort
# 4. Exit
# Enter your choice: 1
# Enter number of vertices: 5
# Enter adjacency matrix (use 0 if no edge):
# Row 0: 0 2 3 0 0
# Row 1: 2 0 1 4 0
# Row 2: 3 1 0 5 6
# Row 3: 0 4 5 0 7
# Row 4: 0 0 6 7 0

#  ---------- MAIN MENU ----------
# 1. Input Graph
# 2. Run Prim's MST Algorithm
# 3. Perform Selection Sort
# 4. Exit
# Enter your choice: 2

# Edge : Weight
# 0 - 1 : 2
# 1 - 2 : 1
# 1 - 3 : 4
# 2 - 4 : 6
# Total Minimum Weight: 13

#  ---------- MAIN MENU ----------
# 1. Input Graph
# 2. Run Prim's MST Algorithm
# 3. Perform Selection Sort
# 4. Exit
# Enter your choice: 3
# Enter number of elements: 6 
# Enter element 1: 34
# Enter element 2: 21
# Enter element 3: 11
# Enter element 4: 45
# Enter element 5: 67
# Enter element 6: 44

# Passes of Selection Sort:

# Pass 1: [11, 21, 34, 45, 67, 44]
# Pass 2: [11, 21, 34, 45, 67, 44]
# Pass 3: [11, 21, 34, 45, 67, 44]
# Pass 4: [11, 21, 34, 44, 67, 45]
# Pass 5: [11, 21, 34, 44, 45, 67]
# Pass 6: [11, 21, 34, 44, 45, 67]

# Sorted Array:
# 11 21 34 44 45 67 

#  ---------- MAIN MENU ----------
# 1. Input Graph
# 2. Run Prim's MST Algorithm
# 3. Perform Selection Sort
# 4. Exit
# Enter your choice: 4
# Exiting Program...
