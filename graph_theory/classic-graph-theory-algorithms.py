# TOPOLOGICAL SORT (TOP SORT) ALGORITHM

# Many read world situations can be modelled as a graph with directed edges where some
# events must occur before others.
#    * School Class Pre-requisites
#    * Program dependencies
#    * Event Scheduling
#    * Assembly instructions

"""
Suppose you are a student at university X and you want to take class H, then you must take
classes A, B, D and E as prerequisites. In this sense, there is an ordering on the nodes
of the graph.

          class C --------\
         /                 \
        /                   \
class A                   class J
       \                   /
        \                 /
        class D ---------/
         /      \
        /         \
       /            \
class B  class E --- class H  
     \
      \
       \ 
       class F ---------- class I

       
If you needed to take all the classes, the top sort algorithm will be capable of telling the order in
which you should enroll in the classes such that you never enroll in a course for which you donot have
the pre-requisites.


Another canonical example where an ordering of the nodes of the graph matters is for program
build dependencies. A program cannot be built unless its dependencies are first built.

   B -------> E ---------> H 
   /       /^  \
  /       /     \v
A -----> D       G ---------> J (want to build program J)
          \     /^
           \v  /
C --------> F -------> I        K
           
One way of ordering program dependencies (nodes) from the above graph is A, C, B, D, F, E, G, H, J (Unused Dependencies K, I)

Topological Sorting is an algorithm that gives us a topological ordering on a directed graph.
A Topological Ordering is an ordering of nodes in a directed graph where for each directed edge from node
'A' to node 'B', node 'A' appears before node 'B' in the ordering.

The Topological Sort algorithm can find a topological ordering in O(V+E) time!
NOTE: Topological Orderings are not Unique! A graph can have multiple Topological Orderings!

Not every Graph can have a topological ordering. A graph which contains a cycle cannot have a valid ordering
(since there is nowhere to start and every node is dependent on another node):

1 ------> 2 --> 4
 \^       |    / \
  \       |v  /   \
   \        3      \
    \     /^        \
     \   /           \v
       0 -----------> 5


The only type of graphs which have a valid topological ordering are Directed Acyclic Graphs (DAGs).
These are graphs with directed edges and no cycles.
By definition, all rooted trees have a topological ordering since they donot contain any cycles.

HOW CAN YOU VERIFY THAT YOUR GRAPH DOES NOT CONTAIN A DIRECTED CYCLE ?
USE TARJAN'S STRONGLY CONNECTED COMPONENT ALGORITHM WHICH CAN BE USED TO FIND THESE CYCLES

STEPS FOR TOPOLOGICAL SORTING:
 * Pick an unvisited node
 * Begining with the selected node, do a Depth First Search (DFS) exploring only unvisited nodes
 * On the recursive callback of the DFS, add the current node to the topological ordering in
   reverse order



PSEUDOCODE FOR TOPOLOGICAL SORTING (TOPSORT) ALGORITHM:

# Assumption: graph is stored as an adjacency list
function topsort(graph)
    N = graph.numberOfNodes()
    V = [false, ..., false] # length N
    ordering = [0, ..., 0] # length N
    i = N - 1 # Index for ordering array

    for (at = 0; at < N; at++)
        if V[at] == false:
            # Since we are dealing with a directed graph, the dfs can end without visiting all the nodes
            # of the graph. How many nodes are visited in one recursive dfs() call depends on the 
            # starting node of the dfs() call. Hence, we loop through all the nodes of the graph and 
            # check if it is visited, and initiate dfs() on the unvisited nodes.
            
            i = dfs(i, at, V, ordering, graph)
    return ordering

# Execute Depth First Search (DFS)
function dfs(i, at, V, ordering, graph):
    V[at] = true
    edges = graph.getEdgesOutFromNode(at)
    for edge in edges:
        if V[edge.to] == false:
            i = dfs(i, edge.to, V, ordering, graph) # recursvie call
    
    # when all children of a node has been visited by recusrive calls or a leaf node is 
    # encountered, add that node to the available memory location from the end of the ordering 
    # array. This way, the order in which the nodes were visited in the recursive callstack of 
    # dfs() is preserved
    
    ordering[i] = at
    return i - 1
"""


# FINDING SHORTEST AND LONGEST PATH IN A DIRECTED ACYCLIC GRAPHS

# Recall that Directed Acyclic Graph (DAG) is a graph with DIRECTED EDGES and NO CYCLES.
# By definition, this means all trees are automatically DAGs since they do not contain cycles

# SINGLE-SOURCE SHORTEST PATH ON A DIRECTED ACYCLIC GRAPH

# The Single Source Shortest Path (SSSP) problem can be solved efficiently on a DAG in O(V+E)
# time. This is due to the fact that the nodes can be ordered in a topological ordering via 
# topsort and processed sequentially.

"""
             11
     B ------------> E
  ^/ | \           /   \
 3/  |   \4    -4/       \9
 /   |     \v  /           \v
A    |4      D --5-> F --1-> H
 \   |    ^/   \            /^
 6\  |   /8     2\        /2
  v\ | /           \v   /
     C ------------>  G
             11

             
Arbitraty Topological Order: A, B, C, D, G, E, F, H

Assuming the source node is A, we have the following distances from node A:

----------------------------------------------------
| 0 | 3 | 6 | 3+4 | 11+6 | 3+4-4 | 3+4+5 | 3+4+2+2 |
----------------------------------------------------
| A | B | C |  D  |   G  |   E   |   F   |    H    |
----------------------------------------------------

"""

# Finding the longest path on a general graph is a NP-Hard problem. But, on a DAG, this problem
# is solvable in O(V+E). The trick is to multiple each edge by -1 then find the shortest path
# and then multiply the edge values by -1 again!

"""
CODE FOR FINDING SHORTEST PATH FROM A SINGLE NODE IN A DIRECTED ACYCLIC GRAPH

// Given an adjacency list, this method finds the shortest path to all nodes starting at 'start'
// NOTE: 'numNodes' is not neccessarily the number of nodes currently present in the adjacency list
// since you can have singleton nodes with no edges which would'nt be present in the adjacency list
// but are still part of the graph!

public static integer[] dagShortestPath(Map<Integer, List<Edge>> graph, int start, int numNodes) {
    int[] topsort = topologicalSort(graph, numNodes);
    Integer[] dist = new Integer[numNodes]; # initialized with null values
    dist[start] = 0; # set the distance from starting node to itself as 0

    for (int i = 0; i < numNodes; i++) {
       int nodeIndex = topsort[i];
       # check to make sure that the node iterated over from the topsort order is not isolated
       # isolated nodes will have the default null value from initialization of dist as they
       # have no edges in the adjacency list
       if (dist[nodeIndex] != null) {
              List<Edge> adjacentEdges = graph.get(nodeIndex);
              # check and prevent issues of isolated nodes with no edges in the graph
              if (adjacentEdges != null) {
                    # Relaxation step (updating distance using current node in the dist array)
                    for (Edge edge: adjacentEdges) {
                            int newDist = dist[nodeIndex] + edge.weight;
                            # if the tail node of the edge is being visited for the first time,
                            # replace null with the calculated distance
                            if (dist[edge.to] == null) dist[edge.to] = newDist;
                            # if the tail node of the edge has already been visited before,
                            # update with the minimum value of its previous distance and the
                            # new calculated distance from the currently processed node
                            else dist[edge.to] = Math.min(dist[edge.to], newDist)
                     }
              }
       }
    }
    return dist;
}

"""





# DIJKSTRA'S SHORTEST PATH ALGORITHM

# This is an important algorithm used to find single source shortest path (SSSP) in graphs with
# non-negative edge weights.
# Depending on how the algorithm is implemented and what data structures are used, the time
# complexity is typically O(E*log(V)) which is competitive agaist other shortest path algorithms.

# One constraint for Dijkstra's algorithm is that the graph must only contain non-negative edge
# weights. This constraint is imposed to ensure that once a node has been visited, its optimal
# distance cannot be improved. This property is especially important because it enables Dijkstra's
# algorithm to act in a greedy manner by always selecting the next most promising node.

# There is a Lazy implementation of this algorithm that uses SP + stopping early optimization.
# There is also an eager implementation of this algorithm that uses indexed priority queue +
# decreaseKey operation to reduce space and increase performance. Other types of heaps can be
# used to further boost the performance of the algorithm (eg: D-ary heaps)

# Quick Overview:
# Maintain a 'dist' array where the distance to every node is positive infinity/null. Mark
# the distance to the start node 's' as 0. 
# Maintain a priority queue of key-value pairs (node index, distance) which tells you the next
# node to visit based on sorted min of the value (distance)
# insert (s, 0) into the priority queue and loop while priority queue is not empty, pulling out
# the next most promising (node index, distance) pair.
# Iterate over all edges outwards from the current node and relax each edge, appending a new 
# (node index, distance) key-value pair to the priority queue for every relaxation (distance updation
# step). The lazy implementation of Djikstra's algorithm has multiple key-value entries for the same
# node in the priority queue (one for each edge of the node). We then lazily delete the outdated
# key-value pairs (edges which lead to a longer path distance than what is currently the minimum from
# the start node)


"""
PSUEDOCODE FOR LAZY IMPLEMENTATION OF DJIKSTRA'S SSSP ALGORITHM (STORES ONLY THE OPTIMAL DISTANCE,
NOT THE PATH). CAN BE USED TO OBTAIN PATH FROM START NODE TO ANY OTHER NODE IN GRAPH.

# Runs Djikstra's algorithm and returns an array that contains
# the shortest distance to every node from the start node 's'
# g - adjacency list of weighted graph
# n - the number of nodes in the graph
# s - the index of the starting node (0 <= s < n)
function djikstra(g, n, s):
    vis = [false, ..., false] # size n
    # array to keep track of the previous node from which the shortest distance
    # was encountered for node at index. This array will be used to trace back
    # the shortest path.
    prev = [null, null, ..., null] # size n
    # set the distance for all nodes as infinity
    dist = [inf, inf, inf, ..., inf] # size n 
    dist[s] = 0 # set the distance from start node to itself as 0
    pq = empty priority queue 
    pq.insert((s, 0))
    while pq.size() != 0:
        # get the next most promising (node index, minimum distance) pair
        index, minValue = pq.pop()
        vis[index] = true # mark the index as visited
        # if the distance value is already greater than the existing distance
        # for the node, ignore the key-value pair (optimization)
        if dist[index] < minValue: continue
        # loop through all the neighbors of the node at the index of the pair
        for (edge: g[index]):
            # continue if the nighboring node is already visited
            if vis[edge.to]: continue
            newDist = dist[index] + edge.cost # Relaxation operation
            # Update the distance for the neighbor node from the start node
            # if the calculated distance from start node via the node at
            # current index is smaller. Then insert this new neighbor index
            # with updated distance into the priority queue so that it will be
            # prioritized and bubbled up to be picked up when this neighbor
            # node is visited for the first time (new pair added everytime
            # distance is updated). This leads to duplicate pairs with the
            # same key in the priority queue (PQ).
            # This is done instead of updating the distance directly for the
            # neighbor node key-value pair in the priority queue because most
            # standard priority queue implementations donot allow updating the
            # value of a key stored in them. Inserting a new key-value pair
            # takes O(logN) time compared to updating an existing value of a key
            # which takes O(N) time because the PQ is sorted by the value and
            # insertion is done by searching for the key.
            if newDist < dist[edge.to]:
                dist[edge.to] = newDist
                prev[edge.to] = index
                pq.insert((edge.to, newDist))
            # stopping early
            # if index == e:
            #     return dist[e]
    return (dist, prev)

    
    # Finds the shortest path between two nodes.
    # g - adjacency list of weighted graph
    # n - number of nodes in the graph
    # s - the index of the starting node (0 <= s <= n)
    # e - the index of the end node (0 <= e <= n)
    function findShortestPath(g, n, s, e):
        dist, prev = djikstra(g, n, s)
        path = []
        # check that end node is reachable
        if (dist[e] == inf) return path
        # begin from the end node and work backwards to the start node along
        # the path array until the start node 's' is reached. Remember, prev[s]
        # will be null because there is no shortest path to itself from any other node.
        for (at = e; at != null; at = prev[at]):
            path.add(at)
        path.reverse() # reverse the path array to start from the start node
        return path
"""


# STOPPING EARLY

# Another optimization that can be done to the above algorithm is stopping early, when you know
# the starting node 's' and destination node 'e' beforehand. In the average case, you 
# don't have to visit every node in the graph in this case to build the distance and 
# previous node arrays for every node. 


# The above implementation of Djikstra's SSSP algorithm is inefficient for dense graphs
# as you will end up with several stale, unused key-value pairs in the priority queue. The
# eager version of the Djikstra's algorithm avoids duplicate key-value pairs and supports
# efficient value updates in O(logN) by using an Indexed Priority Queue (IPQ).


# INDEXED PRIORITRY QUEUE

# An Indexed Priority Queue is a traditional priority queue variant which on top of the
# regular priority queue operations, supports quick updates and deletionsof key-value pairs.
# It allows to quickly lookup and dynamically change values in the priority queue, on the fly.
# A birectional mapping between the N keys of and the domain [0, N) is created for the 
# indexed priority queue using a bidirectional hash table. Keep in mind that priority queues
# are implemented as heaps under the hood, which internally use an arrays and we want to 
# facilitate indexing into this array in the indexed priority queue.
# Often, the keys themselves are integers in the range [0, N), so there is no need for
# the mapping, but it is handy to be able to support any type of key (like names).

# If 'K' is the key we want to update in the indexed priority queue, first we get the
# key's index: ki = map[K], then use 'ki' with the indexed priority queue:
#   * delete(ki) - delete a key
#   * valueOf(ki) - get the value associated with a key
#   * contains(ki) - check if a key exists in the priority queue
#   * peekMinKeyIndex() - get the index of the key with the smallest value
#   * pollMinKeyIndex() - 
#   * peekMinValue() - getting the smallest value in the indexed priority queue
#   * pollMinValue() - 
#   * insert(ki, value) - insert key-value pairs
#   * update(ki, value) - update key-value pairs
#   * decreaseKey(ki, value) - specialized update operations
#   * increaseKey(ki, value) - specialized update operations

# The IPQ can be implemented in several ways using specialized heaps for optimizations.
# Here, we will look at a Binary Heap based implementation where the time complexities
# are either O(1) or O(logN). We will implement a Min IPQ where the key with the lowest
# value is taken out first and assumed to have the highest priority. Each key is assigned
# a unique index value between [0, N). Each key is also assigned its value. To access the
# value for any given key 'k', find its key index (ki) and do a lookup in the 'vals' array
# maintained by the IPQ.

# Recall that a very common way to represent a binary heap is with an array since every
# node is indexed sequentially.

"""
Let 'i' be the current node (zero based).
left child index: 2i + 1 (zero based)
right child index: 2i + 2 (zero based)

TREE REPRESENTATION:

                                  (0)
                                   9
                                  /  \  
                                 /    \
                                /      \
                               /        \
                              /          \
                             /            \ 
                        (!) /              \  (2)
                          8                 7
                        /   \              / \
                      /      \            /   \       
                (3)  6    (4) 5      (5) 1     2 (6)
                    / \       / \       / \
                   /   \     /   \     /   \ 
                  2     2   3     4   0    insertion position to maintain complete tree structure
                (7)    (8)  (9) (10) (11)  (insertion point for all intermediate nodes to have 
                                            two children in the binary tree/heap)

                                            
HEAP REPRESENTATION:

        ---------------------------------------------------------------------
        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12  | 13  |  14 |
        ---------------------------------------------------------------------
        | 9 | 8 | 7 | 6 | 5 | 1 | 2 | 2 | 2 | 3 | 4  |  0 | n/a | n/a | n/a |
        ---------------------------------------------------------------------

Q: What are the children of the node at index 4?
        left child = 2 * 4 + 1 = 9
        right child = 2 * 4 + 2 = 10


Suppose we insert the value '8'. This would violate the heap invatiant (the binary search 
tree invariant where the left child value should be < than parent value and right child value 
should be > parent value). So, we bubble/sift up the value until the heap invariant/binary search 
tree invariant is met:

TREE REPRESENTATION:

                                  (0)
                                   9
                                  /  \  
                                 /    \
                                /      \
                               /        \
                              /          \
                             /            \ 
                        (!) /              \  (2)
                          8                  7
                        /   \              /  \
                      /      \            /    \       
                (3)  6    (4) 5      (5) 1      2 (6)
                    / \       / \       / \    / \
                   /   \     /   \     /   \  /   \
                  2     2   3     4   0    8 
                (7)    (8)  (9) (10) (11) (12)  
                                            

                                            
HEAP REPRESENTATION:

        ---------------------------------------------------------------------
        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12  | 13  |  14 |
        ---------------------------------------------------------------------
        | 9 | 8 | 7 | 6 | 5 | 1 | 2 | 2 | 2 | 3 | 4  |  0 |  8  | n/a | n/a |
        ---------------------------------------------------------------------


In a traditional Priority Queue, to remove items, we search for the element to remove 
and then swap it with the last node (usually the bottom-right most node), perform removal, 
and finally bubble up or down the swapped value at the removal node location (the removal
node is checked for the heap invariant/BST invariant).


INDEXED PRIORITY QUEUE AS A BINARY HEAP:

Supose we have N people with different priorities that we need to serve at. Assume that
the priorities can dynamically change and we always want to serve the person with the 
lowest priority (MinBinaryHeap). To figure out who to serve next, we will use a Min Indexed
Priority Queue to sort by the lowest value first. We will maintain two arrays



---------------                                                            (0) <- index of node in heap
|  Key   | ki |                                                           Henry
---------------                                                         ki=7, v=1 
|  Anna  |  0 |                                                       /           \
---------------                                                      /             \
|  Bella |  1 |                                                     /               \
---------------                                                    /                 \
|  Carly |  2 |                                              (1)  /                   \   (2)
---------------                                                George                Anna
|  Dylan |  3 |                                              ki=6, v=2             ki=0, v=3
---------------                                           /         \              /        \
|  Emily |  4 |                                          /           \            /          \
---------------                                         /             \          /            \
|  Fred  |  5 |                                 (3)    /         (4)   \    (5) /              \ (6)
---------------                                     Isaac           James     Laura           Fred
| George |  6 |                                   ki=8, v=6      ki=9, v=5  ki=11, v=4      ki=5, v=9
---------------                                   /     \           /  \         / \           /  \
| Henry  |  7 |                                  /       \         /    \       /   \         /    \
---------------                                 /         \       /      \     /     \       /      \
| Isaac  | 8  |                         (7)    /     (8)   \  (9)/    (10)\   / (11)  \     /        \
---------------                             Dylan       Emily  Bella   Kelly Carly 
| James  | 9  |                             ki=3        ki=4   ki=1    ki=10 ki=2
---------------                             v=17        v=7    v=15    v=16  v=11
| Kelly  | 10 |
---------------
| Laura  | 11 |
---------------


THE vals ARRAY:

           -------------------------------------------------------------------------------------------
    (ki)   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  11 |  12 |  13 |  14 | 
           -------------------------------------------------------------------------------------------
  vals     |  3  |  15 |  11 | 17  |  7  |  9  |  2  |  1  |  6  |  5  |  16 |  4  |  -1 |  -1 |  -1 |
           -------------------------------------------------------------------------------------------
    
THE pm ARRAY:

           -------------------------------------------------------------------------------------------
    (ki)   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  11 |  12 |  13 |  14 | 
           -------------------------------------------------------------------------------------------
  (heap    |  2  |  9  |  11 |  7  |  8  |  6  |  1  |  0  |  3  |  4  |  10 |  5  |  -1 |  -1 |  -1 |
  index)   -------------------------------------------------------------------------------------------
            
THE im ARRAY:

  (heap    -------------------------------------------------------------------------------------------
  index)   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  11 |  12 |  13 |  14 |
           -------------------------------------------------------------------------------------------
    (ki)   |  7  |  6  |  0  |  8  |  9  |  11 |  5  |  3  |  4  |  1  |  10 |  2  |  -1 |  -1 |  -1 |
           -------------------------------------------------------------------------------------------

Arbitrarily assign each person a unique index value between [0, N) - the 'ki' column. The 
initial values placed inside the IPQ - the 'Values' column will be maintained by the IPQ
dynamically, accounting for insertion, deletion and updation of values. Note that the values 
of the key-value pairs of an IPQ can be any comparable data type, not only integers. 
When we insert (ki, v) pairs into an IPQ, we sort by the value associated with each key.
In the heap above, we are sorting by smallest value, since we are working with a min heap.

A key mapping and inverse lookup mapping is required to access the position of the node for
a particular key in the heap, and to get the key of a node at a particular position in the heap.
This is required because the key index does not actually reflect the position of the node with
the key in the heap!

To access the value for any given key 'k', find its key index (ki) and do a lookup in the 'vals'
array maintained by the IPO
Q: What value does the key 'Bella' have in the IPQ ?
 ki for 'Bella' is 1. So 'Bella' has a value of vals[ki] = vals[1] = 15

Q: How to find the index of the node for a particular key in the IPQ ?
 Maintain a Position Map "pm" to tell the index of the node in the heap for a given key index "ki"

Q: Which node represents the key "Dylan"?
 The key index for "Dylan" is 3. Looking at index 3 in the position map tells that the node for
 key "Dylan" is at position 7 in the heap.

Q: How do we go from knowing the position of a node in the heap, to its key and key index?
 create an inverse map "im" to perform this inverse lookup of node index in heap to the key index
 "ki" and the key.

Q: Which key is present in the node at index 2 in the heap?
 A lookup in the inverse map "im" at index 2 gives a key index 0. From this, we can get the key
 which is "Anna".


Insertion and Deletion of keys in an Indexed Priority Queue is similar to a regular priority queue,
except for the additional requirement of maintaining the position map and inverse lookup map with
to reflect the changes caused by these operations (including the bubble-up/sink-down operations -
when two nodes are swappe in the heap during these operations, "pm" and "im" values are also 
swapped correspondingly. Note that since only the nodes are swapped, the key index and values 
remain untouched)


PSEUDOCODE FOR IMPLEMENTATION OF AN INDEXED PRIORITY QUEUE/MIN INDEXED BINARY HEAP

# Inserts a value into the min indexed binary
# heap. The key index must not already be in
# the heap and the value must not be null
function insert(ki, value):
  values[ki] = value
  # 'sz' is the current size of the heap
  pm[ki] = sz
  im[sz] = ki
  swim(sz) # bubble-up the newly inserted node 
  # from the bottom-most right position in
  # the binary tree to its corresponding
  # position
  sz = sz + 1

# swims up node i (zero based) until heap
# invariant is satisfied (the parent node
# must have lower value than the child node)
function swim(i):
  for (p = (i - 1) / 2; i > 0 and less(i, p)):
    # get the index (p) of the parent of node
    # at 'i' and compare their values. swap
    # the node picked from 'i' with the previous
    # layer's parent until the node at 'i' is
    # bubbled-up to its appropriate position
    # in the min indexed binary heap
    swap(i, p)
    i = p # new position of node picked up from index 'i'
    p = (i - 1) / 2 # new parent

# swap the node indices in the position map 
# array first and then in the inverse 
# lookup array
function swap(i, j):
  pm[im[j]] = i
  pm[im[i]] = j
  tmp = im[i]
  im[i] = j
  im[j] = tmp

# compare values nodes at two indices in the heap
# and return a boolean which indicates if 
# the first node's values is lesser than the
# second node's value.
function less(i, j):
  return values[im[i]] < values[im[j]]


Polling (remove and return key-value pair with the lowest priority or the root node) in an IPQ 
still has O(logN) time complexity (the root node is swapped with the bottom-rightmost), but Removing a key-value pair in an IPQ is 
improved from O(N) in a traditional priority queue, to O(logN) since node position
lookups are O(1), but repositioning is still O(logN) 
"""

 