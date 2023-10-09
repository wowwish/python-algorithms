# The Breadth First Search (BFS) algorithm is another fundamental search algorithm used to explore
# nodes and edges of a graph. It runs with a time complexity of O(V+E) and is often used as a
# building block in other algorithms.
# The BFS algorithm is particularly useful for one thing: finding the shortest path on an unweighted
# graph.
# A BFS starts at some arbitrary node of a graph and explores the neighbor nodes first, before
# moving to the next level neighbours. In essence, the BFS explores nodes in layers, by maintaining
# a queue (FIFO) datastructure to keep track of which node to visit next. Upon reaching a new node, the 
# algorithm adds it to the queue to visit it later. The queue data structure works just like a 
# real world queue such as a waiting line at a restaurant. People can either enter the waiting line
# (enqueue) or get seated (dequeue).

"""
PSEUDOCODE FOR BREADTH FIRST SEARCH

# Global/Class scope variables
n = number of nodes in the graph
g = adjacency list representing unweighted graph


# s = start node, e = end node, and 0 <= e, s < n
function bfs(s, e):
    # Do a BFS starting at node s
    prev = solve(s)

    # Return reconstructed path from s -> e
    return reconstructPath(s, e, prev)

    
function solve(s):
    q = queue data structure (LIFO) with enqueue and dequeue
    q.enqueue(s)

    visited = [false, ..., false] # size n
    visited[s] = true

    prev = [null, ..., null] # size n
    while !q.isEmpty():
        node = q.dequeue()
        neighbors = g.get(node)

        for (next: neighbors):
            if !visited[next]:
                q.enqueue(next)
                visited[next] = true
                prev[next] = node
    return prev

function reconstructPath(s, e, prev):
    # Reconstrut path going backwards from e
    path = []
    for (at = e; at != null; at = prev[at]): # prev[s] will be null 
        path.add(at)

    path.reverse() # since we go from end node to start, reverse the path

    # If s and e are connected, return the path
    if path[0] == s:
        return path
    return []
"""


# BFS Shortest Path on a Grid:

# Many problems in graph theory can be represented using a grid. Grids are a form of "implicit graph"
# because we can determine a node's neighbours based on our location within the grid. A type of problem
# that involves finding a path through a grid is solving a maze! Another example could be routing
# through obstacles (trees, rivers, rocks etc.) to get to a location!

# A common approach to solving graph theory problems on grids is to first convert the grid to a familiar
# format such as an adjacency list/matrix.
# IMPORTANT: Assume the grid is unweighted and cells connect left, right, up and down.
# We will first label the cells in the empty grid with numbers [0, n) where n = no. of rows x no. of columns
# Then, we construct an adjacency list/matrix. Once we have this adjacency list/matrix, we can run
# whatever specialized graph algorithm to solve our problem such as: shortest path, connected components, etc... 
# However, transformation between graph representations can usually be avoided due to the structure and
# nature of a grid: we can move left, right, up and down from a cell in the middle of the grid to move
# to adjacent cells.

# Mathematically, from a cell at (r, c), we can access its four adjacent cells using Direction Vectors:
# (r - 1, c), (r + 1, c), (r, c - 1) and (r, c + 1). If the problem you are trying to solve allows
# moving diagonally, we can also access the four additional cells (r - 1, c - 1), (r - 1, c + 1), 
# (r + 1, c - 1) and (r + 1, c + 1).

# This makes it very easy to access neighbouring cells from the current row-column position.

"""
# Define the Direction Vectors for north, south, east and west
dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

for (i = 0; i < 4; i++):
    rr = r + dr[i]
    cc = c + dc[i]
    
    # Skip invalid cells that are out of bounds of the grid. 
    # Assume R and C for the number of rows and columns in the grid.
    if rr < 0 or cc < 0: continue
    if rr >= R or cc >= C: continue
    
    # (rr, cc) is a neighbouring cell of the cell at (r, c)
"""


# Let's solve a shortest path problem in a grid using the Direction Vectors method:

# DUNGEON PROBLEM STATEMENT:
# You are trapped in a 2D dungeon and need to find the quickest way out! The dungeon
# is composed of unit cubes which may or may not be filled with rock. It takes one
# minute to move one unit north, south, east, west. You cannot move diagonally and
# the maze is surrounded by solid rock on all sides. Is an escape possible ? If so, 
# how long will it take ?

# The Dungeon has a size of R x C and you start in cell 'S' and there's an exit at cell 'E'.
# A cell full of rock is indicated by a '#' and empty cells are represented by a '.'. Remember
# that you need the shortest path to escape the dungeon and not just any path! For this, you 
# can count the number of cells you encounter along your BFS based path. Also be mindful of the
# scenario where you might not have a path that leads to the exit from the start!
# Remember that you could also terminate the algorithm early if you reach the exit cell before
# visiting all the cells of the grid, leaving behind some unvisited cells!

"""
                  C
      0   1   2   3   4   5   6
     -----------------------------
   0 | S | . | . | # | . | . | . |
     -----------------------------                          
   1 | . | # | . | . | . | # | . |
     -----------------------------
R  2 | . | # | . | . | . | . | . |
     -----------------------------
   3 | . | . | # | # | . | . | . |
     -----------------------------
   4 | # | . | # | E | . | # | . |
     -----------------------------
    
"""

# We Start at the start node coordinate by adding (sr, sc) to the queue in BFS. 
# Then, we visit the adjacent unvisited neighbours and add them to the queue as well.
# We continue this process while not adding cells with rocks to the queue.
# Remember that you could also terminate the algorithm early if you reach the exit cell before
# visiting all the cells of the grid, leaving behind some unvisited cells!
# Similar to BFS, we use a 2D prev matrix to generate the path by retracing our steps.
# NOTE: BFS is only good for finding the shortest path in an unweighted graph. On a weighted
# graph, a longer path may actually result in a shorter overall weight/value, while on an
# unweighted graph, all edges are assumed to be of constant value (ie, a weight of 1) so the
# shortest path is guaranteed to be found. DFS can only find an arbitrary path between two
# nodes on an unweighted graph and this path may not neccessarily be the shortest path.

# ALTERNATIVE STATE REPRESENTATION:
# So far, we have been storing the next x-y position in the queue as an (x, y) pair. This
# works well but requires either an array or an object wrapper to store the coordinate values.
# In practice, this requires a lot of packing of values to and from the queue. We can use an
# alternative approach which also scales well in higher dimensions and requires less setup
# effort: Use one Queue for each Dimension! - so in a 3D grid, you would have one queue for
# each of the x, y and z dimensions. One thing to keep in mind here, is to enqueue and dequeue
# all of the coordinate queues at the same time.

"""
PSEUDOCODE FOR THE DUNGEON PROBLEM:

# Global/Class scope variables
R, C = ... # R = number of Rows, C = number of Columns
m = ... # Input character matrix of size R x C
sr, sc = ... # row and column values for the cell with the 'S' symbol
rq, cq = ... # Empty Row Queue (RQ) and Column Queue (CQ)

# Variables used to track the number of steps taken
move_count = 0 # actually tracks the number of steps taken
nodes_left_in_layer = 1 # tracks how many nodes we need to dequeue before taking a step
nodes_in_next_layer = 0 # tracks how many nodes we added in the BFS expansion and is used to
# update nodes_left_in_layer accordingly in the next iteration of BFS

# Variable used to track whether the 'E' character ever gets reached during the BFS
reached_end = False

# R x C matrix of false values used to track whether the node at position (i, j) has been visited
visited = ...

# north, south, east, west direction vectors
dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

function solve():
    # Get the start cell row and column and mark the start cell as visited
    rq.enqueue(sr)
    cq.enqueue(sc)
    visited[sr][sc] = true

    # Perform iterative BFS until either the row queue or column queue is empty
    while rq.size() > 0: # or cq.size() > 0
        r = rq.dequeue()
        c = cq.dequeue()
        if m[r][c] == 'E':
            reached_end = true
            break
        explore_neighbours(r, c) # Add all valid unvisited neighbours of current node to the row and column queue
        nodes_left_in_layer--

        # Increment the number of steps taken everytime we finish a layer of adjacent nodes in the grid
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count++
    if reached_end:
        return move_count
    return -1

function explore_neighbours(r, c):
    for (i = 0; i < 4; i++):
        rr = r + dr[i]
        cc = c + dc[i]

        # Skip out of bounds locations
        if rr < 0 or cc < 0: continue
        if rr >= R or cc >= C: continue

        # Skip visited locations or blocked cells with rocks
        if visited[rr][cc]: continue
        if m[rr][cc] == '#': continue

        rq.enqueue(rr)
        cq.enqueue(cc)
        visited[rr][cc] = true
        nodes_in_next_layer++
"""