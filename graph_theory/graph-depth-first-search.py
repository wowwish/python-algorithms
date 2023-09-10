# The Depth First Search (DFS) is the most funamental search algorithm used to explore nodes
# and edges of a graph. It runs with a time complexity of O(V + E) and is often used as a
# building block in other algorithms.
# By itself, the DFS is isn't all that useful, but when augmented to perform other tasks
# such as counting connected components, determining connectivity, or finding bridges/articulation
# points, then DFS really shines.
# As the name suggests, a DFS plunges depth first into a graph without regard for which edge it
# takes next until it cannot go any further at which point, it backtracks and continues.

"""
PSEUDOCODE FOR DFS USING RECURSION:

# Global or class scope variables
n = number of nodes in the graph
g = adjacency list representing the graph
visited = [false, ..., false] # size n

function dfs(at):
    if visited(at): return
    visited(at) = true

    neighbours = graph(at)
    for next in neighbours:
        dfs(next) # recursion

# start DFS at node 0
start_node = 0
dfs(start_node)
"""


# DFS is used in finding Connected Components:

# Sometimes a graph is split into multiple disjoint (individual components contain many connected nodes
# that all will share the same ID, the word "disjoint" here means that the individual components 
# of the graph are not connected to each other) components. It's useful to be able to identify and 
# count these components. One way to identify them is to colour them, so that we can tell them apart.
# Colouring components means, to assign an unique integer (or ID) to the group of nodes that 
# constitute each component of the graph. 
#   * We first make sure that all the nodes are labelled from [0, N) where N is the number of nodes.
#   * We can use a DFS to identify components. The basic algorithm is to start a DFS at every node,
#   unless the node has been already visited, and mark all the reachable nodes as being part of the
#   same component using the same unique ID.


"""
PSEUDOCODE FOR FINDING CONNECTED COMPONENTS:

# Global or class scope variables
n = number of nodes in the graph
g = adjacency list representing graph
count = 0 # Disjoint Component (group of nodes) ID
components = empty integer array that contains component ID (count) for each node # size n
visited = [false, ..., false] # size n

function findComponents():
    for (i = 0; i < n; i++)
        if !visited[i]:
            count++ # increment component ID
            dfs(i) # This function is a variant of DFS that visits all connected nodes to a given node to assign an ID
    return (count, components)

function dfs(at):
    visited[at] = true
    components[at] = count # assign same component ID to the connected node within the component
    for (next : g[at]):
        if !visited[next]:
            dfs(next) # Recursive call
"""

# We can also augment the DFS algorithm to:

#   * Compute a Graph's minimum spanning tree (MST).
#   * Detect and find cycles in a graph.
#   * Check if a graph is Bipartite.
#   * Find strongly connected components.
#   * Topologically sort the nodes of a graph.
#   * Find bridges and articulation points.
#   * Find augmenting paths in a flow network.
#   * Generate mazes.