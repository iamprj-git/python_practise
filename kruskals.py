# Helper class to represent a graph edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight


# Helper class to represent a disjoint set
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


# Function to find the minimum spanning tree using Kruskal's algorithm
def kruskal(graph):
    # Sort all the edges in non-decreasing order of their weights
    sorted_edges = sorted(graph, key=lambda x: x.weight)

    # Create an empty set to store the MST
    mst = []

    # Create a disjoint set to keep track of connected components
    disjoint_set = DisjointSet(range(len(graph)))

    # Iterate through the sorted edges
    for edge in sorted_edges:
        src_root = disjoint_set.find(edge.src)
        dest_root = disjoint_set.find(edge.dest)

        # Check if including the edge creates a cycle
        if src_root != dest_root:
            mst.append(edge)
            disjoint_set.union(src_root, dest_root)

    return mst


# Example usage
# Create a graph using Edge objects
edges = [
    Edge(0, 1, 4),
    Edge(0, 7, 8),
    Edge(1, 2, 8),
    Edge(1, 7, 11),
    Edge(2, 3, 7),
    Edge(2, 8, 2),
    Edge(2, 5, 4),
    Edge(3, 4, 9),
    Edge(3, 5, 14),
    Edge(4, 5, 10),
    Edge(5, 6, 2),
    Edge(6, 7, 1),
    Edge(6, 8, 6),
    Edge(7, 8, 7)
]

# Find the minimum spanning tree
minimum_spanning_tree = kruskal(edges)

# Print the edges in the minimum spanning tree
for edge in minimum_spanning_tree:
    print(f"{edge.src} -- {edge.dest}: {edge.weight}")
