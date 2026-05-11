import java.util.*;

    class GraphColoring {

        private int V;
        private int[][] graph;
        private int[] colors;

        private String[] colorNames = {"", "Red", "Green", "Blue"};

        public GraphColoring(int[][] adjacencyMatrix, int numColors) {
            V = adjacencyMatrix.length;
            graph = adjacencyMatrix;
            colors = new int[V];
        }

        private boolean isSafe(int v, int c) {
            for (int i = 0; i < V; i++) {
                if (graph[v][i] == 1 && colors[i] == c) {
                    return false;
                }
            }
            return true;
        }

        private boolean solveGraphColoring(int v, int m) {
            if (v == V) {
                printSolution();
                return true;
            }

            for (int c = 1; c <= m; c++) {
                if (isSafe(v, c)) {
                    colors[v] = c;

                    if (solveGraphColoring(v + 1, m)) {
                        return true;
                    }

                    colors[v] = 0;
                }
            }
            return false;
        }

        private void printSolution() {
            System.out.println("Vertex Colors:");
            for (int i = 0; i < V; i++) {
                System.out.println("Vertex " + i + " -> " + colorNames[colors[i]]);
            }
        }

        public void solve(int m) {
            if (!solveGraphColoring(0, m)) {
                System.out.println("No solution exists.");
            }
        }

        public static void main(String[] args) {

            int[][] graph = {
                {0, 1, 1, 1},
                {1, 0, 1, 0},
                {1, 1, 0, 1},
                {1, 0, 1, 0}
            };

            int numColors = 3;

            GraphColoring gc = new GraphColoring(graph, numColors);
            gc.solve(numColors);
        }
    }