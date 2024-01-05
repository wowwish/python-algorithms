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





"""

SHORTEST PATH (SP) ALGORITHMS:-


                            BFS               DIJKSTRA'S             BELLMAN-FORD        FLOYD-WARSHALL

                            
                            
COMPLEXITY               O(V + E)             O((V+E) * LogV)         O(V * E)             O(V^3)



RECOMMENDED GRAPH          LARGE              LARGE/MEDIUM            MEDIUM/SMALL         SMALL       
   SIZE



GOOD FOR ALL SOURCE       ONLY WORKS ON           OKAY                   BAD               YES
  SHORTEST PATH?        UNWEIGHTED GRAPHS



CAN DETECT NEGATIVE             NO                  NO                   YES               YES
      CYCLES?              




SHORTEST PATH ON GRAPH     INCORRECT SHORTEST     BEST ALGORITHM        WORKS             BAD IN
WITH WEIGHTED EDGES?           PATH ANSWER                                                GENERAL




SHORTEST PATH ON GRAPH        BEST ALGORITHM          OKAY               BAD              BAD IN
WITH UNWEIGHTED EDGES?                                                                    GENERAL


NOTE:  For a Directed Acyclic Graph (DAG), a combination of Topological Sorting with Dynamic
Programming will run in O(V+E). It uses the fact that we can obtain a topological ordering on the
nodes of the graph since it is a DAG and uses DP to find the shortest path and it the fastest solution
for finding shortest path in a DAG.
"""





# FINDING SHORTEST AND LONGEST PATH IN DIRECTED ACYCLIC GRAPHS

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
# step). The lazy implementation of Dijkstra's algorithm has multiple key-value entries for the same
# node in the priority queue (one for each edge of the node). We then lazily delete the outdated
# key-value pairs (edges which lead to a longer path distance than what is currently the minimum from
# the start node)


"""
PSUEDOCODE FOR LAZY IMPLEMENTATION OF DIJKSTRA'S SSSP ALGORITHM (STORES ONLY THE OPTIMAL DISTANCE,
NOT THE PATH). CAN BE USED TO OBTAIN PATH FROM START NODE TO ANY OTHER NODE IN GRAPH.

# Runs Dijkstra's algorithm and returns an array that contains
# the shortest distance to every node from the start node 's'
# g - adjacency list of weighted graph
# n - the number of nodes in the graph
# s - the index of the starting node (0 <= s < n)
function dijkstra(g, n, s):
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
        dist, prev = dijkstra(g, n, s)
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

# USING AN INDEXED PRIORITY QUEUE

# The above implementation of Dijkstra's SSSP algorithm is inefficient for dense graphs
# as you will end up with several stale, unused key-value pairs in the priority queue. The
# eager version of the Dijkstra's algorithm avoids duplicate key-value pairs and supports
# efficient value updates in O(logN) by using an Indexed Priority Queue (IPQ).



"""
PSEUDOCODE FOR THE LAZY IMPLEMENTATION OF DJISKTRA'S SSSP ALGORITHM.
CANNOT BE USED TO OBTAIN PATH FROM START NODE TO ANY OTHER NODE IN GRAPH.

# Runs Dijkstra's algorithm and returns an array that contains
# the shortest distance to every node from the start node 's'
# g - adjacency list of weighted graph
# n - the number of nodes in the graph
# s - the index of the starting node (0 <= s < n)
function dijkstra(g, n, s):
    vis = [false, ..., false] # size n
    # set the distance for all nodes as infinity
    dist = [inf, inf, inf, ..., inf] # size n 
    dist[s] = 0 # set the distance from start node to itself as 0
    ipq = empty indexed priority queue 
    ipq.insert((s, 0))
    while ipq.size() != 0:
        # get the next most promising (node index, minimum distance) pair
        index, minValue = ipq.poll()
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
            # current index is smaller, then insert this new neighbor index
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
                # if the vertex at edge end is not in the indexed priority queue, 
                # insert the key-value pair into the indexed priority queue. Otherwise,
                # use the decreaseKey() function to update the distance of existing key
                # only when it is lower than pre-existing key.
                if !ipq.contains(edge.to):
                  ipq.insert((edge.to, newDist))
                else:
                  ipq.decreaseKey(edge.to, newDist)
            # stopping early
            # if index == e:
            #     return dist[e]
    return dist
    
"""



# D-ARY HEAP OPTIMIZATION


# When executing Dijkstra's algorithm, especially on dense graphs, there are a lot more updates 
# (ie, ipq.decreaseKey() operations) to key-value pairs than there are dequeue (poll) operations.
# A D-ary heap is a heap variant in which each node has 'D' children. This speeds up ipq.decreaseKey()
# operations at the expense of more costly removals in a D-ary heap based Indexed Priority Queue when
# it is used to implement the Dijkstra's algorithm. This is because once the value is updated for a key,
# the swim() steps take lesser runtime, the higher the number 'D' is for the heap (A higher
# 'D' value flattens the heap, leading to lesser child-parent value comparisons when bubbling up
# a node). However, when we want use sink(), the runtime is increased with higher 'D'
# values due to the number of children for each node in the heap. Each child's value has to be compared 
# with the parent node's value during swapping.


# WHAT IS THE OPTIMAL D-ARY HEAP DEGREE 'D' TO OPTIMIZE PERFORMANCE OF DIJKSTRA'S ALGORITHM ?

# In general, the average degree D = E/V (E = number of edges, V = number of nodes) is the best 'D' 
# to use to balance removals against decreaseKey() operations improving Dijkstra's time complexity to 
# O(E*log_e/v(V)) which is much better especially for dense graphs which have lots of decreaseKey() 
# operations.
# State of the art implementations of Dijkstra's algorithm use the Fibonacci Heap which gives it 
# a time complexity of O(E + Vlog(V)). However, in practice, Fibonacci heaps are very diffiult to
# implement and have a large enough constant amortized overhead to make them impractical unless 
# your graph is quite large.



# SOURCE CODE FOR EAGER IMPLEMENTATION OF DIJKSTRA'S ALGORITHM

"""
import static java.lang.Math.max;
import static java.lang.Math.min;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.NoSuchElementException;

public class DijkstrasShortestPathAdjacencyWithDHeap {
    
    // An edge class to represent a directed edge
    // between two nodes, with a certain cost or weight.
    public static  class Edge {
        int to;
        double cost;
        // Constructor for inner class
        public Edge(int to, double cost) {
            this.to = to;
            this.cost = cost;
        }
    }

    private final int n;

    private int edgeCount;
    private double[] dist;
    private Integer[] prev;
    private List<List<Edge>> graph;

    /**
    * Initialize the solver by providing the graph size and a starting node.
    * Use the addEde() method to actually add edges to the graph.
    * n - number of nodes in the graph.
    */
    public DijkstrasShortestPathAdjacencyListWithDHeap(int n) {
        // Main class constructor
        this.n = n;
        createEmptyGraph();
    }

    // create an empty graph (Adjacency list) with 'n' nodes including the source and sink nodes
    public void createEmptyGraph() {
        graph = new ArrayList<>[n];
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
    }

    /**
    * Adds a directed edge to the graph
    * from - the index of the node where the added directed edge will start at
    * to - the index of the node where the added directed edge will end at
    * cost - the cost or weight of the edge
    */
    public void addEdge(int from, int to, int cost) {
        edgeCount++; // count of the edges in the graph is incremented
        graph.get(from).add(new Edge(to, cost));
    }

    /**
    * Use the addEdge() method to add edges to the graph and use this method to retrieve
    * the constructed graph.
    */
    public List<List<Edge>> getGraph() { 
        return graph;
    }

    // Run Dijkstra's Algorithm on a directed graph to find the shortest path
    // from a starting node to an ending node. If there is no path between the
    // starting node and the destination node, the returned value is set to be
    // double.POSITIVE_INFINITY
    // Although the algorithm can be used to get the minimum distance to every
    // node in the graph from the start node, having the end node allows us to
    // do early stopping optimization.
    public double dijkstra(int start, int end) {
        // Keep an indexed priority queue (IPQ) constructed using a D-ary Heap
        // optimized for this graph.
        int degree = edgeCount / n; // Thre 'D' value for creating the IPQ
        MinInsertDHeap<Double> iqp = new MinInsertDHeap(degree, n);
        // set the distance for start from itself to 0.0
        ipq.insert(start, 0.0);

        // Maintain an array of the minimum distance to each node.
        dist = new double[n];
        // initialize min distances to all nodes as infinity
        Arrays.fill(dist, double.POSITIVE_INFINITY);
        dist[start] = 0.0; // set the minimum distance of the starting node from itself to 0
        
        boolean[] visited = new boolean[n];
        prev = new Integer[n]; // for reconstructing the shortest path

        // pick each high-priority (min distance) unvisited (novel) node from the IPQ
        while(!ipq.isEmpty()) {
            int nodeId = ipq.peekMinKeyIndex();
            // set the node obtained from the IPQ as visited
            visited[nodeId] = true;
            double minValue = ipq.pollMinValue(); // get the value from the IPQ for node
            
            // If we already have found a better path before we got to
            // processing this novel node, we can ignore it
            if (minValue > dist[nodeId]) continue;
            for (edge:Edge : graph.get(nodeId)) {
                
                // We cannot get a shorter path by revisiting
                // a node that we have already visited before
                if (visited[edge.to]) continue;

                // Relax edge by updating minimum cost (distance) if applicable
                double newDist = dist[nodeId] + edge.cost;
                // if the cost of visiting any other node in the graph is reduced
                // by moving through our novel node, update the new minimum distance
                // to the destination node and add the current novel node as predecessor
                // for the SSSP from start node to the destination node in 'prev' array
                // Remember that the 'dist' is set to positive infinity values except
                // the start node (which has 0.0). Hence, the first time a novel node
                // is visited, the distance will be the current minimum distance to the
                // novel node.
                if (newDist < dist[edge.to]) {
                    prev[edge.to] = nodeId;
                    dist[edge.to] = newDist;
                    
                    // Insert the cost of going to the destination node in the IPQ if the IPQ
                    // does not have a key-value pair for the destination node. If a key-value
                    // pair exists, try and update it to a better value by calling ipq.decrease()
                    if (!ipq.contains(edge.to)) {
                        ipq.insert(edge.to, newDist);
                    }
                    else {
                        // if the destination node has already been visited, only
                        // update the value in the IPQ for the destination node
                        // if 'newDist' < its current value. This is another optimization
                        // of the algorithm where IPQs are handy
                        ipq.decrease(edge.to, cost);
                    }
                }

                // Once we've processed the end node, we can return early (without
                // necessarily visiting the whole graph) because we know we cannot get a
                // shorted path by routing through any other nodes since Dijkstra's is
                // greedy and there are no negative edge weights.
                if (nodeId == end) return dist[end];
            }
        }
        // If end node is unreachable, and all the key-value pairs of the IPQ 
        // have been processed, return postive infinity
        return Double.POSITIVE_INFINITY;
    }

    /**
    * Reconstructs the shortest path (of nodes) from the 'start' node to 'end' node
    * inclusive. It returns an array of node indices of the shortest path from 'start'
    * to 'end'. If 'start' and 'end' are not connected, then an empty array is returned.
    */
    public List<Integer> reconstructPath(int start, int end) {
        if (end < 0 || end >= n) {
            throw new IllegalArgumentException("Invalid node index");
        }
        if (start < 0 || start >= n) {
            throw new IllegalArgumentException("Invalid node index");
        }
        List<Integer> path = new ArrayList<>();
        double dist = dijkstra(start, end);
        if (dist == Double.POSITIVE_INFINITY) return path; // handle unreachable 'end' node
        // traverse from 'end' node to 'start' node using the 'prev' array
        for (Integer at = end; at != null; at = prev[at]) {
            path.add(at);
        }
        // reverse the path because it is currently from end to start
        Collections.reverse(path);
        return path; // return the constructed path
    }
}
"""





# BELLMAN-FORD ALGORITHM


# In graph theory, the Bellman-Ford (BF) algorithm is a Single Source Shortest Path (SSSP)
# algorithm. This means, it can find the shortest path from one node to any other node in
# the graph.
# However, BF is not ideal for most SSSP problems because it has a time complexity of O(E * V).
# It is better to use Dijkstra's algorithm with a binary heap (much faster with
#  O(E+V) * LogV) time complexity).
# We can still use the BF algorithm in situations where the Dijkstra's algorithm fails, such
# as in the case of graphs with negative edge weights. Here, BF becomes very handy because it
# can be used to detect Negative Cycles and determine where they occur.
# Finding Negative Cycles can be useful in many types of applications eg. in finance when
# performing arbitrage between two or more markets, where you would rely on edges with negative
# weights to obtain a net gain. However, the presence of negative cycles in the graph makes it 
# ill-suited problem for shortest path finding and the BF Algorithm can be used to detect such
# graphs.

# Negative Cycles can manifest in many ways: 
# * self loops: Nodes with self-loops make all the adjacent nodes to potentially have negative
#   infinity as the min distance for SSSP.
# * net cost: Another form of Negative-Loops is a group of connected nodes whose costs/weights
#   add up to a negative number. Such Negative Cycles usually affect most of the nodes in the graph.
#   eg: Node1 -> Node2: 1, Node2 -> Node3: 4, Node3 -> Node1 -> -6


# Bellman-Ford Algorithm Steps:
# * Let E = number of Edges, V = number of Vertices, S = id of starting node,
#   D = array of size 'V' that tracks the best distance from 'S' for each node.
# * Set every entry in 'D' to positive infinity
# * Set 'D[S] = 0'
# * Iteratively Relax/update distances in 'D' using each edge. Note that we iterate V - 1
#   times and update 'D' by processing every edge of the graph. Also, the edges do not have to 
#   be chosen in any particular order from the graph, we can randomly pick edges for every 
#   iteration and will still arrive at the same min distance from the start node to all other nodes.
#   We run the two iterations V - 1 times (degrees of freedom), because we want the second iteration 
#   that sets negative infinity to propogate throught the graph. When we are looking for shortest 
#   paths, if a directed graph has 'V' number of vertices then the longest such path without a cycle 
#   can have all the 'V' vertices, at the maximum. Consequently, such a path will have (V - 1) edges. 
#   Since the longest possible path without a cycle can be (V - 1) edges, the edges must be scanned 
#   (V - 1) times to ensure the shortest path has been found for all nodes. With each run of the two 
#   iterations, one vertex gets its minimum distance while there is a chance for some other vertex 
#   to not have its distance be cauculated through the minimum distance path of its predecessor vertex.
#   
#   for (i = 0; i < V - 1; i = i + 1):
#       for edge in graph.nodes:
#           // Relax edge (update D with shorter path)
#            if (D[edge.from] + edge.cost < D[edge.to]):
#               D[edge.to] = D[edge.from] + edge.cost
#   // Repeat second time to find nodes caught in Negative Cycles. If the minimum distance
#   // seems to be lesser for the same node upon a second iteration, it means that the node
#   // is part of a Negative Cycle and is undergoing a cumulative effect on the minimum distance.
#   // to fix this issue we set the distance for such nodes as negative infinity in this second
#   // iteration. This prevents further updation of the distance array 'D' for the vertex as the
#   // vertex is part of, or is affected by negative cycles. The other vertices directly connected
#   // to this vertex will also have propogation of the negative infinity value in subsequent 
#   // iterations of the algorithm.
#   // NOTE: we may need to add additional logic to differentiate between nodes that are directly
#   // part of a negative cycle and nodes whose distance values are affected by the presence of 
#   // a negative cycle. The method used here does not differentiate between the two.
#   // As an example logic, we can use the Strongly-Connected Components Algorithm of Tarjan to
#   // detect the direct Negative Cycle nodes (get SCCs before running BF and then run BFS/DFS from
#   // any of the constituent node of the SCCs that seem to have nodes updated to negative infinity 
#   // in BF to get the direct Negative Cycle nodes) and the remaining nodes detected in the second 
#   // iteration of BF would be the affected nodes.
#   for (i = 0; i < V - 1; i = i + 1):
#       for edge in graph.edges:
#           if(D[edge.from] + edge.cost < D[edge.to])
#                D[edge.to] = negative infinity
#
# * A final scan of all edges is performed is to detect negative cycles in the graph. This final
#   scan simply runs the second iteration of the previous step and if any distance in 'D' is updated
#   in this scan, then a path of length 'V' edges has been found, which can only occur when the graph
#   has negative cycles.

# Dijkstra's algorithm uses a priority queue to greedily select the closest vertex that has not yet 
# been processed, and performs this relaxation process on all of its outgoing edges; by contrast, the 
# Bellman-Ford algorithm simply relaxes all the edges and does this ∣V∣−1 times, where ∣V∣ is the number 
# of vertices in the graph. In each of these repetitions, the number of vertices with correctly 
# calculated distances grows, from which it follows that eventually, all vertices will have their 
# correct distances. This method allows the Bellman-Ford algorithm to be applied to a wider class of 
# inputs than Dijkstra. 


"""
BELLMAN-FORD ALGORITHM IN ACTION


                -50       -10
            6 -------> 7 ------> 8
            ^ \^                /^
            |   \             /
         60 |     \ 5       / 50
            |       \     /
      5     |         \ / 
0 --------> 1 -------> 5          9 
            |     30   |         /^
            |          |       /
         20 |       25 |     / 100
            |          |   /
  10        V          v /
3 <=======> 2 -------> 4
         -15     75



First iteration over all the edges of the graph: V = 0:

        -------------------------------------------------------------
        |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
        -------------------------------------------------------------
        |  0  |  5  | 20  | 35  | 60  |  35 |  40 | -10 | -20 | 200 |
        -------------------------------------------------------------
                   (35 - 15)

Second iteration over all the edges of the graph: V = 1:

        -------------------------------------------------------------
        |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |
        -------------------------------------------------------------
        |  0  |  5  | -i  | -i  | -i  |  35 |  40 | -10 | -20 | -i  |
        -------------------------------------------------------------




SOURCE CODE FOR BELLMAN-FORD ALGORITHM ON A GRAPH IMPLEMENTED AS AN EDGE LIST:

/**
* An implementation of the Bellman Ford Algorithm. The Algorithm finds
* the shortest path between a starting node and all other nodes in the graph.
* The algorithm also detects negative cycles. If a node is part of a negative
* cycle, then the minimum cost for that node is set to Double.NEGATIVE_INFINITY.
*/
public class BellmanFordEdgeList {

    // A directed Edge inner class
    public static class Edge {
        double cost;
        int from, to;
        
        // Constructor for inner class
        public Edge(int from, int to, double cost) {
            this.from = from;
            this.to = to;
            this.cost = cost;
        }
    }

    public static doble[] BellmanFord(Edge[] edges, int V, int start) {
        
        double dist[] = new double[V];
        java.util.Arrays.fill(dist, Double.NEGATIVE_INFINITY);
        dist[start] = 0;

        // For each vertex, apply relaxation for all the edges
        for (int v = 0; v < V - 1; v++) {
            for (Edge edge : edges) {
                if (dist[edge.from] + edge.cost < dist[edge.to]) {
                    dist[edge.to] = dist[edge.from] + edge.cost;
                }
            }
        }

        // Run algorithm a second time to detect which nodes
        // are part of a negative cycle. A negative cycle has
        // occured if we can find a better path beyond the
        // optimal solution. Nodes that are either directly part
        // of a negative cycle or that are affected by a negative
        // cycle will have Double.NEGATIVE_INFINITY after the algorithm
        // fully completes all iterations (since adding any number to negative
        // infinity will return negative infinity itself).
        for (int v = 0; v < V - 1; v++) {
            for (Edge edge : edges) {
                if (dist[edge.from] + edge.cost < dist[edge.to]) {
                    dist[edge.to] = Double.NEGATIVE_INFINITY;
                }
            }
        }

        // Return the array containing the shortest distance to every node
        return dist;
    }
}

"""





# FLOYD-WARSHALL ALL PAIRS SHORTEST PATH ALGORTIHM


# In graph theory, the Floyd-Warshall (FW) algorithm is an All-Pairs Shortest Path (APSP)
# algorithm. This means, it can find the shortest path between all pairs of nodes in the graph.

# NOTE:The time complexity to run FW is O(V^3) which is ideal for graphs no larger than a couple
# of hundred nodes!  

# With the FW Algorithm, the optimal way to represent a graph is by using the 2D Adjacency Matrix
# 'm' where cell 'm[i][j]' represents the edge weight of going from node 'i' to node 'j'. If there
# is no edge from node 'i' to node 'j', then set the edge value for 'm[i][j]' to be positive infinity.
# NOTE: if your programming language does not support a special constant for positive infinity such
# that positive infinity + positive infinity = positive infinity, 
# and x + positive infinity = positive infinity, then avoid using (2^31 - 1; integer's maximum value) 
# as infinity! This will cause integer overflow; prefer to use a large constant such as 10^7 instead. 
# If you really need a true "infinite" value, you could also try using a double or a float data type 
# for the adjacency matrix.

# The main idea behind the Floyd-Warshall algorithm is to gradually build up all intermediate
# routes between nodes 'i' and 'j' to find the optimal path. Suppose our adjacency matrix tells
# us that the distance from vertex 'a' to vertex 'b' is: m[a][b] = 11, and suppose there exists
# a third vertex 'c' such that m[a][c] + m[c][b] < m[a][b], then it is better to route through
# 'c'! The goal of FW is to eventually consider going through all possible intermediate vertices
# on paths of different lengths. For example, going 'c' -> 'b' might itself involve going through
# one or more intermediate vertices that minimizes the distance between 'c' and 'b'!

# The algorithm uses dynamic programming to cache optimal solutions in a "memo table" and updates
# the values in the table as new and better optimal solutions are found. Let 'dp' (short for) Dynamic
# Programming) be a 3D matrix of size n x n x n that acts as a memo table.
# Then,
#       dp[k][i][j]  = shortest path from 'i' to 'j' found by routing through nodes {0, 1, ..., k-1, k}
# Start with k = 0, then use that solution to calculate shortest distances at k = 1, then use that 
# solution to calculate shortest distance at k  = 2 and so on. The shortest path between 'i' to 'j' is
# updated for the current value of 'k' only when the distance is shorter than the previous best solution
# calculated considering each of the k-1 nodes from 0 to k-1.
# This gradually builds up the optimal solution routing through 0, then all optimal solutions
# routing through 0 and 1, then all optimal solutions routing through 0, 1, 2 ... etc up until n-1 which
# stores the all-pair shortest path solution. Specifically, dp[n-1] is the 2D matrix solution that we
# are after.
# In the begining, the optimal solution from i to j in the 'dp' table is simply the distance in
# the adjacency matrix.
#       dp[k][i][j] = m[i][j] if k = 0, where 'm' is the adjacency matrix
#       dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j]) if k > 0
#                                                       ^
#                                                       |
#                                                       |
#                               Find the best distance from 'i' to 'j' by finding minimum of 
#                                    distance when rerouting through node 'k' and the best solution
#                                       calculated through previous iterations of dynamic programming
#                                            by rerouting from k=0, k=1, ..., k=k-1.

# Currently, we're using O(V^3) memory since our memo table 'dp' has one dimension for each of 'k', 
# 'i' and 'j'. Notice that we will be looping over 'k' starting from 0, then 1, then 2 and so on. The
# important thing to note here is that the current iteration's result builds off the previous iteration's
# result since we need state at 'k-1' to compute state at 'k'. However, it is possible to compute
# the solution for each iteration in-place using only a single 2D matrix, saving us a dimension of 
# memory and reducing the space complexity to O(V^2)! This will look like this:
#       dp[i][j] = m[i][j] if k = 0, where 'm' is the adjacency matrix
#       dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]) if k > 0


"""
PSEUDOCODE FOR FLOYD-WARSHALL ALL PAIRS SHORTEST PATH ALGORITHM


# Global/Class scope variables
n = size of the adjacency matrix
dp = the memo table that will contain APSP solution
next = matrix used to reconstruct shortest paths

function floydWarshall(m):
    setup(m)

    # Execute FW all pairs shortest path algorithm
    for (k:= 0; k < n; k++):
        for (i := 0; i < n; i++):
            for (j := 0; j < n; j++):
                if (dp[i][k] + dp[k][j] < dp[i][j]):
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next[i][j] = next[i][k]

    # detect and propogate negative cycles
    propogateNegativeCycles(dp, n)

    # Return APSP matrix
    return dp

function setup(m):
    dp = empty matrix of size n x n. This will hold the same datatype of 'm' (Int/Float)

    # The path reconstruction matrix 'next' should contain null values by default
    next = empty integer matrix of size n * n

    # do a deepcopy of the input matrix and setup
    # the 'next' matrix for path reconstruction
    for (i := 0; i < n; i++):
        for (j= 0; j < n; j++):
            # initialize the solution matrix 'dp' with the values of input matrix 'm'
            dp[i][j] = m[i][j]
            # for any finite distance value in the input matrix 'm', set the intermediate node
            # for path from 'i' to 'j' as 'j' itself initially.
            if m[i][j] != +inf:
                next[i][j] = j


            
SOURCE CODE FOR FLOYD-WARSHALL ALGORITHM:

import java.util.ArrayList;
import java.util.List;

public class FloydWarshallSolver {
    /* Example-usage */

    // Create a graph with 'n' nodes. The dajacency matrix is constructed
    // such that the value of goinf from a node to iself is 0.
    public static double[] [] createGraph(int n) {
        double[][] mat = new double[n][[n];
        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(matrix[i], POSITIVE_INFINITY);
            matrix[i][i] = 0;
        }
        return matrix;
    }

    public static void main(String[] args) {
        // construct graph with 7 nodes as an example
        int n = 7;
        double[][] m = createGraph(n);

        // add some edge values
        m[0][1] = 2;
        m[0][2] = 5;
        m[0][6] = 10;
        m[1][2] = 2;
        m[1][4] = 11;
        m[2][6] = 2;
        m[6][5] = 11;
        m[4][5] = 1;
        m[5][5] = -2;

        floydWarshallSolver solver = new floydWarshallSolver(m);
        double[][] dist = solver.getApspMatrix();

        for (int i = 0; i < n; i++) {
            for int (j = 0; i < n; j++) {
                System.out.printf("The shortest path from node %d to node %d is %.3f\n", i, j, dist[i][j]);
                // prints:
                // The shortest path from node 0 to node 0 is 0.000
                // The shortest path from node 0 to node 1 is 2.000
                // The shortest path from node 0 to node 2 is 4.000
                // The shortest path from node 0 to node 3 is infinity
                // The shortest path from node 0 to node 4 is -infinity
                // The shortest path from node 0 to node 5 is -infinity
                // The shortest path from node 0 to node 6 is 0.000
                // The shortest path from node 1 to node 0 is infinity
                // The shortest path from node 1 to node 1 is 1.000
                // The shortest path from node 1 to node 2 is 2.000
                // The shortest path from node 1 to node 3 is infinity
                // ...
            }
            System.out.println();
        }

        // Reconstruct the hosrtest paths from  all node to every other node
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                List<Integer> path = solver.reconstructShortestPath(i, j);
                String str;
                if (path == null) {
                    str = "HAS AN INFINITE NUMBER OF SOLUTIONS! (Negative Cycle Case)";
                } else if (path.size() == 0) {
                    str = String.format("DOES NOT EXIST (node %d does'nt reach node %d)", i, j);
                } else {
                    str = String.join(" -> ", path.stream()
                                                  .map(object::toString)
                                                  .collect(java.util.stream.Collectors.toList()));
                    str = "is: [" + str + "]";
                }

                System.out.println("The shortest path from node %d to node %d %s\n", i, j, str);

                // Prints:
                // The shortest path from node 0 to node 0 is: [0]
                // The shortest path from node 0 to node 1 is: [0 -> 1]
                // The shortest path from node 0 to node 2 is: [0 -> 1 -> 2]
                // The shortest path from node 0 to node 3 DOES NOT EXIST (node 0 does'nt reach node 3)
                // The shortest path from node 0 to node 4 HAS INFINITE SOLUTIONS! (Negative Cycle Case)
                // The shortest path from node 0 to node 5 HAS INFINITE SOLUTIONS! (Negative Cycle Case)
                // The shortest path from node 0 to node 6 is: [0 -> 1 -> 2 -> 6]
                // The shortest path from node 1 to node 0 DOES NOT EXIST (node 1 does'nt reach node 0)
                // The shortest path from node 1 to node 1 is: [1]
                // The shortest path from node 1 to node 2 is: [1 -> 2]
                // The shortest path from node 1 to node 3 DOES NOT EXIST (node 1 does'nt reach node 3)
                // The shortest path from node 1 to node 4 HAS INFINITE SOLUTIONS! (Negative Cycle Case)
                // The shortest path from node 1 to node 5 HAS INFINITE SOLUTIONS! (Negative Cycle Case)
                // The shortest path from node 1 to node 6 is: [1 -> 2 -> 6]
                // The shortest path from node 2 to node 0 DOES NOT EXIST (node 2 does'nt reach node 0)
                // ...
            }
        }
    }
    private int n;
    private boolean solved;
    private double[][] dp;
    private Integer[][] next;
    
    private static final int REACHED_NEGATIVE_CYCLE = -1;

    /**
    * As input, this class takes an adjacency matrix with edge weights between nodes,
    * where POSITIVE_INFINITY is used to indicate that two nodes are not connected.
    *
    * NOTE: Usually the diagonal of the adjacency matrix is all zeros
    * (ie, matrix[i][i] = 0 for all i) since there is typically no cost
    * to go from a node to itself, but this may depend on your graph and
    * the problem you are trying to solve.
    */
    private floydWarshallSolver(double[][] matrix) {
        n = matrix.length;
        dp = new double[n][n];
        next = new Integer[n][n];

        # Copy input matrix and setup 'next' matrix for path reconstruction
        for (int i =0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] != POSITIVE_INFINITY) {
                    next[i][j] = j;
                }
                dp[i][j] = matrix[i][j];
            }
        }
    }

    /**
    * Runs Floyd-Warshall Algorithm to compute the shortest distance between every pair of nodes
    * Returns the solved All Pairs Shortest Path (APSP) matrix.
    */
    public double[][] getApspMatrix() {
        if (!solved) solve();
        return dp;
    }

    // Execute the Floyd-Warshall Algorithm
    public void solve() {
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dp[i][k] + dp[k][j] < dp[i][j]) {
                        dp[i][j] = dp[i][k] + dp[k][j];
                        next[i][j] = next[i][k];
                    }
                }
            }
        }

        // Identify Negative Cycles by propogating the value 'NEGATIVE_INFINITY'
        // to every edge that is part of, or reaches into a negative cycle
        // The same approach of second-iteration from Bellman-Ford Algorithm
        // is used here also to detect node that are part of, or participate in
        // negative cycles. Basically, if we can improve upon the previously computed best
        // solution after all iterations, then the node pair is connected by
        // a shortest path through a negative cycle!
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dp[i][k] + dp[k][j] < dp[i][j]) {
                        dp[i][j] = NEGATIVE_INFINITY;
                        next[i][j] = REACHES_NEGATIVE_CYCLE;
                    }
                }
            }
        }
        
        solved = true;
    }

    /**
    * Reconstructs the shortest path (of nodes) from 'start' to 'end' inclusive
    * 
    * Returns an array of node indexes of the shortest path from 'start' to 'emd'.
    * If 'start' and 'end' are not connected, returns an empty array. If the shortest
    * path from 'start' to 'end' is through a negative cycle, returns -1.
    */
    public List<Integer> reconstructShortestPath(int start, int end) {
        if (!solved) solve();
        List<Integer> path = new ArrayList<>();
        // If the 'end' node is not reachable from the 'start' node as indicated by 
        // 'POSITIVE_INFINITY' value in the 'dp' matrix, then return the empty 'path' array
        if (dp[start][end] == POSITIVE_INFINITY) return path;
        int at = start;
        for (; at != end; at = next[at][end]) {
            // Return null since there are an infinite number of shortest paths through
            // a negative cycle
            if (at == REACHES_NEGATIVE_CYCLE) return null;
            // Otherwise, add the intermediate node index to 'path' array
            path.add(at);
        }
        // Return null since there are an infinite number of shortest paths through
        // a negative cycle. Handling the 'end' node to 'end' node case here.
        if (next[at][end] == REACHES_NEGATIVE_CYCLE) return null;
        path.add(end);
        // Otherwise, add the 'end' node index to 'path' array
        return path;
    }
}

"""








# BRIDGES AND ARTICULATION POINTS


# A bridge / cut edge is any edge in a graph whose removal increases the number of connected
# components (similar to bridges connecting islands on a map) in the graph.
# An Articulation point / cut vertex is any node in the graph whose removal increases the number
# of connected components.

"""


            0                       6
          /   \                   /   \
         /     \                /       \
        1 ----- 2 ----------- 5           7
               /                \       /
              /                   \   /
             3 -------- 4           8
                
        BRIDGES: 3 -> 2, 3 -> 4, 2 -> 5 (when these edges are cut, it leads to one or more connected components)
        ARTICULATION POINTS: 2, 5, 3 (when these nodes are removed, it leads to one or more connected components) 

"""    

# Bridges and Articulation points are important in graph theory because they often hint at weak points,
# bottlenecks or vulnerabilities in a graph. Therefore, it's important to be able to quickly 
# find/detect when and where these occur.
# Finding both bridges and articulation points can be achieved using a similar algorithm since both
# problems are related.


# Bridge finding Algorithm:
# * Before starting the DFS, initialize the low-link values of all the vertices to be the ids of
#   the vertices.
#   NOTE: The low-link value of a node is defined as the smallest (lowest) id reachable (even through 
#   intermediated nodes) from that node using forward edges (the end node of the edge is a descendant 
#   of the start node and can be several levels deep in the DFS tree) and back edges (the end node of
#   the edge is an ancestor of the start node several levels above in the DFS tree) when doing a DFS, 
#   including the id of the node itself!
# * Start at any node and do a Depth First Search (DFS) traversal, converting undirected edges into 
#   directed ones, and labelling nodes with an increasing id value as you go. Mark each node encountered
#   during the DFS as visited and skip visited nodes in subsequent iterations/recursive calls of the
#   DFS. Keep track of the id of each node and the smallest low-link value for the node. 
#   NOTE: DFS on an undirected graph converts the graph into a tree with forward and back edges. 
# * During the DFS, BRIDGES WILL BE FOUND WHERE THE ID OF THE NODE YOUR EDGE IS STARTING FROM IS 
#   LESS THAN THE LOW-LINK VALUE OF THE NODE YOUR EDGE IS GOING TO (This means, your edge's starting
#   node is from one connected component where all the constituent nodes have one low-link value, and 
#   the end node of the edge is from another connected component which starts from a node with 'id'
#   higher than the start node's connected component - hence the higher low-link value for the end node
#   of the edge than the start node's id). 



"""
LOW-LINK VALUE VISUALIZATION:

INITIALIZATION:

            (0)                    (6)
            0                       6
          /   \                   /   \
         /     \ (2)        (5) /       \ (7)
    (1) 1 ----- 2 ----------- 5           7
               /                \       /
              /                   \   /
        (3) 3 -------- 4 (4)       8 (8)

        

ASSIGNED LOW-LINK VALUE AFTER DFS (REMEMBER THAT THE EDGES ARE MADE DIRECTED DURING THE DFS):

            (0)                    (5) 
            0                       6
          /   \^                 ^/   \
        v/     \ (0)        (5) /      v\ (5)
    (0) 1 ----> 2 ----------> 5           7
               /               ^\       /
            v/                   \   /v
        (3) 3 -------> 4 (4)       8 (5)


    *   2 -> 0 is a back edge that forms a cycle in the graph (0 is ancestor of 2)
    *   6 -> 5 can be considered as an imaginary forward edge (5 is descendant of 6) in 
            the 6 -> 7 -> 8 -> 5 -> 6 cycle. Notice that all nodes in this cycle are assigned
            a low-link value of 5 since node 5 is reachable through a path from any of these edges
            using the directed edges created by the DFS!
    *   2 -> 5 is a cross edge (connects two nodes that donot have any ancestor or descendant relationship)

    * Notice that that the condition for a directed edge 'e' to be a bridge
      is when the id of the start node of the edge is lesser than the low-link value of the end node
      of the edge, eg: 2 -> 5 where the id 2 < 5 which is the low-link value of node '5'.
    * Other similar examples of edges which form bridges include: 2 -> 3, 3 -> 4
      When the edge is part of a single graph component, both the start and end nodes of the edge
      will have the lowest id node in the graph component. When the edge is a bridge, it will have
      a starting node with a smaller low-link value (the smallest id in the first component) than the
      ending node (which will have the smallest id in the second component).
    * Due to the order of DFS, the starting node will always have a low-link value < ending node 
      for a bridge!
    * For example, if a new edge 8 -> 2 was added to the above graph, then the edge 2 -> 5 will
      no longer be a bridge because the low-link value of node with id '8' becomes 2.
"""

# The runtime complexity of such an algorithm to find bridges can be optimized to O(V + E) by
# performing one complete DFS to label all the nodes and also find all the low-link values.


"""

PSEUDOCODE FOR BRIDGE FINDING ALGORITHM:

id = 0
g = adjacency list with undirected edges
n = size of the graph

# In these arrays, index 'i' represents node with id 'i'
ids = [0, 0, ..., 0] # Length n to store node ids
low = [0, 0, ..., 0] # Length n to store low-link values of nodes
visited = [false, false, ..., false] # Length n to keep track of whether a node has been visited by dfs

function findBridges():
    bridges = []
    # find all bridges in the graph across
    # various connected components
    # iterate through all nodes of the graph
    for (i = 0; i < n; i = i + 1):
        # perform dfs if the node is not yet visited
        # multiple main dfs() calls can occur because the graph
        # can have two or more isolated connected components with bridges as well
        if (!visited[i]):
            # the main DFS call has no parent node and so, the parent is set as -1
            # However, subsequent recursive calls of dfs() calls spawned by this main call 
            # will have a valid parent node id
            dfs(i, -1, bridges)
    return bridges


# Perform Depth First Search (DFS) to find bridges.
# at = current node id, parent = id of previous node.
# The bridges array is always of even length and 
# indexes (2*i, 2*i+1) form a bridge. For example,
# nodes at indexes (0, 1) are a bridge, (2, 3) is 
# another etc...
function dfs(at, parent, bridges):
    # mark current node as visited
    visited[at] = true
    # increment the globally scoped 'id' variable to keep track of id of nodes
    id = id + 1
    # initialize the low-link value and id for current node
    low[at] = ids[at] = id

    # iterate over the edges starting from the current node 'at' and ending at other nodes 
    # represented by the iteration variable 'to'
    for (to: g[at]):
        # in this recursive DFS implementation, we will come across an edge of the current node
        # that ends at the previous node from which this current recursive call was executed.
        # we want to ignore such cases.
        if to == parent: continue
        if (!visited[to]):
            # when the end node of current node's valid edge is not visited,
            # do a recursive call
            dfs(to, at, bridges) # recursive call
            # propogate the low-link of current node as the minimum of the current node
            # and its recursive calls to its adjacent nodes
            # Keep in mind that the low-link value will be propagated from the inner-most
            # recursive call to this main call. This is how nodes in a cycle are assigned 
            # the lowest node id in the cycle as their low-link value
            low[at] = min(low[at], low[to])
            if (ids[at] < low[to]):
                bridges.add(at)
                bridges.add(to)
        # An already visited adjacent neighbor node connected to current node can also have a low-link
        # value that is smaller than the current node's low-link value. So we address this case
        # here
        else:
            low[at] = min(low[at], ids[to])

"""


# ARTICULATION POINTS

# Articulation points are related very closely to bridges. It won't take much modification to the
# finding bridges algorithm to find articulation points. On a connected component with three or 
# more vertices, if an edge (u, v) is a bridge, then either 'u' or 'v' is an articulation point.
# However, this condition alone is not sufficient to capture all articulation points. There exists
# cases where there is an articulation point without a bridge.


"""

ARTICULATION POINTS WITHOUT ANY BRIDGE:

            (0)            (3)                  1 (0)
                0           3                   ^ \ 
                | \^     ^/ |                   |   \
                |   \   /   |                   |     \v
                |     2 (0) |               (0) 0       2 (0)
                |  ^/   \   |                   |      /
               v| /      v\ |v                  |    /
                1           4                   v  /v
               (0)          (4)                 3 (0)


    In the above graph, there are no bridges, but node '2' is an articulation point since
    its removal would cause the graph to split into two connected components!
    Such situations occur when there are cycles in the graph, as the lowest id of the (starting) node
    in the cycle will be propagated as the low-link value to all the nodes involved in the cycle
    in DFS!
    Hence, if id(edge.from) == lowlink(edge.to), then there was a cycle. The indication of a cycle
    back to the origination node of DFS implies an articulation point somewhere in the cycle which 
    will connect the cycle (connected component) to another connected component in the graph. However,
    this is not applicable when the origination node of DFS in the cycle has 0 or 1 outgoing edges 
    (as seen in node with id '0' in the second graph shown above).

    

PSEUDOCODE FOR FINDING ARTICULATION POINTS:

id = 0
g = adjacency list with undirected edges
n = size of the graph
# keep track of the out edges of every origin/root node of a connected component in DFS
outEdgeCount = 0 

# In these arrays, index 'i' denotes node 'i'
low = [0, 0, ..., 0] # Length n
ids = [0, 0, ..., 0] # Length n
visited = [false, false, ..., false] # Length n
isArt = [false, false, ..., false] # Length n

function findArtPoints():
    # find all bridges in the graph across
    # various connected components
    # iterate through all nodes of the graph
    for (i = 0; i < n; i = i + 1):
        # perform dfs if the node is not yet visited
        # multiple main dfs() calls can occur because the graph
        # can have two or more isolated connected components with bridges as well
        if (!visited[i]):
            # Reset edge count for every connected component that initiates a main call of dfs()
            outEdgeCount = 0
            # Start the dfs() call with the current connected component's origin node as root, 
            # the same origin node as current node and since the origin node has no parent, we 
            # pass -1 for parent node id
            dfs(i, i, -1)
            # set the current node as articulation point if the number of edges going out of a 
            # node that is part of the connected component is > 1
            isArt[i] = (outEdgeCount > 1)
    return isArt


# Perform DFS to find articulation points
function dfs(root, at, parent):
    if (parent == root): outEdgeCount++
    # mark the current node in the dfs() call stack being processed as visited
    visited[at] = true
    # Initialization - increment node id and set it as the current node's low-link value 
    # as well as current node's 'id'
    id = id + 1
    low[at] = ids[at] = id

    # For each edge from node 'at' to node 'to'
    for (to : g[at]):
        # in this recursive DFS implementation, we will come across an edge of the current node
        # that ends at the previous node from which this current recursive call was executed.
        # we want to ignore such cases.
        if (to == parent): continue
        if (!visited[to]):
            # when the end node of current node's valid edge is not visited,
            # do a recursive call
            dfs(root, to, at)  # recursive call
            # propogate the low-link of current node as the minimum of the current node
            # and its recursive calls to its adjacent nodes
            # Keep in mind that the low-link value will be propagated from the inner-most
            # recursive call to this main call. This is how nodes in a cycle are assigned 
            # the lowest node id in the cycle as their low-link value
            low[at] = min(low[at], low[to])
            # Articulation point found via bridge - mark all nodes that are part of a 
            # bridge as articulation points
            if (ids[at] < low[to]):
                isArt[at] = true
            # Articulation point found via cycle - if the low-link value of the end node
            # of the edge is the id of the starting node itself, then the start node of the edge
            # is the origin node of a cycle (connected component) and since it will have the lowest
            if 
            if (ids[at] == low[to]):
                isArt[at] = true
        # An already visited adjacent neighbor node connected to current node can also have a low-link
        # value that is smaller than the current node's low-link value. So we address this case
        # here
        else:
            low[at] = min(low[at], ids[to])
"""




# SOURCE CODE TO FIND BRIDGES


"""

/**
* Finds all the bridges on an undirected graph
**/

import static java.lang.Math.min;
import java.util.ArrayList;
import java.util.List;

public class BridgesAdjacencyList {
    // 'n' is number of nodes in the graph
    // 'id' is a global variable to set newly visited node's id
    private n, id;
    // array of int value to keep track of order of node ids visited in dfs and 
    // the corresponding low-link values
    private int[] low, ids;
    // array of boolean values to keep track of visited nodes
    private boolean[] visited;
    // empty graph
    private List<List<Integer>> graph;

    public BridgesAdjacencyList(List<List<Integer>> graph, int n) {
        if (graph == null || n <= 0 || graph.size() != n)
            throw new IllegalArgumentException();
        this.graph = graph;
        this.n = n;
    }

    // Returns a list of pairs of nodes indicating which nodes form bridges.
    // The returned list is always of even length and indexes (2*i, 2*i+1) form a
    // pair. For example, nodes at indexes (0, 1) are a pair forming a bridge and nodes
    // at indexes (2, 3) are another pair forming a bridge etc ...
    public List<Integer> findBridges() {
    
        // These variables are initialized here instead of inside the constructor of this class to
        // save up memory in case this class is instantiated, but the instance object remains unused
        id = 0;
        low = new int[n]; // low link values
        ids = new int[n]; // node ids
        visited = new boolean[n];

        List<Integer> bridges = new ArrayList<>();

        // Finds all bridges in the graph across various connected components
        for (int i = 0; i < n; i++) 
            if (!visited[i])
                dfs(i, -1, bridges);
        return bridges
        }

        public void dfs(int at, int parent, List<Integer> bridges) {
            
        visited[at] = true; # mark the current node as visited
        low[at] = ids[at] = ++id; # initialize 'id' and low-link value of current node


        // Iterate through all the edges of node 'at' in the graph
        for (Integer to : graph.get(at)) {
            // ignore cases where the edge is from current node to the parent node
            // from which the current recursive dfs() call was initiated
            if (to == parent) continue;
            if (!visited[to]) {
                // recursive call on unvisited new nodes with
                // current node as parent
                dfs(to, at, bridges);
                // propagate low-link value across recursive calls to all the nodes
                // of the current connected component
                low[at] == min(low[at], low[to]);
                // if the id of the start node 'at' is less than the low-link value of
                // the end node 'to' of the current edge, then the current edge is a bridge
                // and we add both the node to the 'bridges' array
                if (ids[at] < low[to]) {
                    bridges.add(at);
                    bridges.add(to)
                }
            }
            else {
                // An already visited adjacent neighbor node connected to current node can 
                // also have a low-link value that is smaller than the current node's low-link 
                // value. So we address this case here
                low[at] = min(low[at], ids[to])
            }
        }
    }
}


/* Example Usage */

public static void main(String[] args) {
    int n = 9; # Create a graph with 9 nodes as an example
    List<List<Integer>>graph = createGraph(n);

    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 2);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);
    addEdge(graph, 2, 5);
    addEdge(graph, 5, 6);
    addEdge(graph, 6, 7);
    addEdge(graph, 7, 8);
    addEdge(graph, 8, 5);

    BridgesAdjacencyList solver = new BridgesAdjacencyList(graph, n);
    List<Integer> bridges = solver.findBridges();

    // Prints:
    // Bridge between nodes: 3 and 4
    // Bridge between nodes: 2 and 3
    // Bridge between nodes: 2 and 5
    for (int i = 0; i < bridges.size() / 2; i++) {
        int node1 = bridges.get(2 * i);
        int node2 = bridges.get(2 * i + 1);
        System.out.printf("Bridge between nodes: %d and %d\n", node1, node2);
    }

    // Initialize graph with 'n' nodes for testing
    public static <List<List<Integer>> createGraph(int n) {
        <List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        return graph;
    }

    // Add undirected edge to given graph adjacency list for testing
    public static void addEdge(List<List<Integer>> graph, int from, int to) {
        graph.get(from).add(to); # forward direction edge from start node to end node
        graph.get(to).add(from); # reverse direction edge from end node to start node
    }
}

"""



# SOURCE CODE TO FIND ARTICULATION POINTS


"""

/**
* Finds all the Articulation Points on an undirected graph
**/

import static java.lang.Math.min;
import java.util.ArrayList;
import java.util.List;

public class ArticulationPointsAdjacencyList {
    // 'n' is number of nodes in the graph
    // 'id' is a global variable to set newly visited node's id
    // 'rootNodeOutcomingEdgeCount' is the number of outgoing edges from the root/starting node
    // of a connected component when walk
    private n, id, rootNodeOutcomingEdgeCount;
    // array of int value to keep track of order of node ids visited in dfs and 
    // the corresponding low-link values
    private int[] low, ids;
    // arrays of boolean values to keep track of visited nodes and articulation points found
    private boolean[] visited, isArticulationPoint;
    // empty graph
    private List<List<Integer>> graph;

    public ArticulationPointsAdjacencyList(List<List<Integer>> graph, int n) {
        if (graph == null || n <= 0 || graph.size() != n)
            throw new IllegalArgumentException();
        this.graph = graph;
        this.n = n;
    }

    // Returns the indexes for all articulation points in the given graph even if the
    // graph is not fully connected
    public List<Integer> findArticulationPoints() {
    
        // These variables are initialized here instead of inside the constructor of this class to
        // save up memory in case this class is instantiated, but the instance object remains unused
        id = 0;
        low = new int[n]; // low link values
        ids = new int[n]; // node ids
        visited = new boolean[n];
        isArticulationPoint = new boolean[n];

        // Finds the atriculation points in the graph across various connected components
        for (int i = 0; i < n; i++) 
            if (!visited[i])
                // reset the outgoing edges from the new origin node of a connected component
                // and initiate a main dfs() call on the root/origin node
                rootNodeOutcomingEdgeCount = 0 // to keep track of outgoing edges from origin node of a connected component
                dfs(i, i, -1);
                // the node at index i in the 'ids' array is an articulation point only if
                // its outcoming edge count is > 1
                isArticulationPoint[i] = (rootNodeOutcomingEdgeCount > 1);
        return isArticulationPoint;
        }

        public void dfs(int root, int at, int parent) {
            
            // if the parent of current node is the root/origin node of a connected component
            // in the DFS traversal of the graph, then increment
            if (parent == root) rootNodeEdgeCount++;

            visited[at] = true; // mark the current node as visited
            low[at] = ids[at] = id++; // initialize 'id' and low-link value of current node

            // Iterate through all the edges of node 'at' in the graph
            List<Integer> edges = graph.get(at);
            for (Integer to : edges) {
                // ignore cases where the edge is from current node to the parent node
                // from which this recursive dfs() call was initiated
                if (to == parent) continue;
                if (!visited[to]) {
                    // recursive call on unvisited new nodes with
                    // current node as parent
                    dfs(root, to, at);
                    // propagate low-link value across recursive calls to all the nodes
                    // of the current connected component
                    low[at] == min(low[at], low[to]);
                    // if the id of the start node 'at' is less than the low-link value of
                    // the end node 'to' of the current edge, then the current edge is a bridge
                    // and we add both the node to the 'bridges' array. For cycles that can also
                    // form bridges, the id of node 'at' will be equal to the low-link value of node 
                    // 'to' and this scenario is also used to mark articulation points from the cycle
                    // which may not have any bridges
                    if (ids[at] <= low[to]) {
                        isArticulationPoint[at] = true;
                    }
                } else {
                    // An already visited adjacent neighbor node connected to current node can 
                    // also have a low-link value that is smaller than the current node's low-link 
                    // value. So we address this case here
                    low[at] = min(low[at], ids[to])
                }
            }
        }
    }
}


/* Example Usage */

public static void main(String[] args) {
    int n = 9; # Create a graph with 9 nodes as an example
    List<List<Integer>>graph = createGraph(n);

    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 2);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);
    addEdge(graph, 2, 5);
    addEdge(graph, 5, 6);
    addEdge(graph, 6, 7);
    addEdge(graph, 7, 8);
    addEdge(graph, 8, 5);

    ArticulationPointsAdjacencyList solver = new ArticulationPointsAdjacencyList(graph, n);
    boolean[] isArticulationPoint = solver.findArticulationPoints();

    // Prints:
    // Node 2 is an articulation point
    // Node 3 is an articulation point
    // Node 5 is an articulation point
    for (int i = 0; i < isArticulationPoint.size() / 2; i++) {
        if (isArticulationPoint[i])
            System.out.printf("Node %d is an articulation point\n", i);
    }

    // Initialize graph with 'n' nodes for testing
    public static <List<List<Integer>> createGraph(int n) {
        <List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        return graph;
    }

    // Add undirected edge to given graph adjacency list for testing
    public static void addEdge(List<List<Integer>> graph, int from, int to) {
        graph.get(from).add(to); # forward direction edge from start node to end node
        graph.get(to).add(from); # reverse direction edge from end node to start node
    }
}

"""






# TARJAN'S ALGORITHM FOR FINDING STRONGLY CONNECTED COMPONENTS


# Strongly Connected Components (SCCs) can be thought of as self-contained cycles within a directed
# graph where every vertex in a given cycle can reach every other vertex in the same cycle. There
# will be no path that leaves a strongly connected component in the directed graph and then goes
# right back into the same component, ie, the stromgly connected components in a graph are unique.

# REMEMBER: low-link value of a node in a graph is the smallest/lowest node id reachable from
# that node when doing a Depth-First Search (including the id of the node in question itself).
# Note that the 'id' for a node is assigned according to the order in which it is processed in the 
# DFS traversal of the graph, with all nodes of a strongly-connected component typically getting
# the same low-link value.

# IMPORTANT: Depending on where the DFS starts, and the order in which nodes/edges are visited,
# the low-link values for identifying SCCs could be wrong. In the context of Tarjan's SCC 
# algorithm, we maintain an invariant that prevents SCCs to interfere with the low-link value
# of other SCCs.

"""

EXAMPLE ERROR CASE SCENARIO WITH LOW-LINK VALUES

                    6 ------------- 4 ------------ 1
                    |              /|              | \
                    |            /  |              |   \
                    |          /    |              |     \
                    |        /      |              |      0
                    |      /        |              |     /
                    |    /          |              |   /
                    |  /            |              | /
                    5 ------------- 3 ------------ 2

                Started DFS on the rightmost node '0', resumed DFS on node '2', and
                then resumed DFS on node '4' to finish labelling all nodes in the graph



                   (0)             (0)             (0)
                    6 ------------> 4 -----------> 1
                    ^              /|             ^| \^
                    |            /  |              |   \
                    |          /    |              |     \v
                    |        /      |              |      0 (0)
                    |      /        |              |     /^
                    |    /          |              |   /
                    | v/            v              | /
                    5 ------------> 3 <----------> 2
                  (0)              (0)             (0)

                All nodes have the same low-link value which is totally wrong!
                There are clearly multiple SCCs in the graph!
                    
"""

# To cope with the random traversal order of the DFS, Tarjan's algorithm maintains a set
# (often as a stack) of valid nodes from which to update low-link values from. Nodes are
# added to this stack (set) of valid nodes as they are explored for the first time.
# Nodes are removed from the stack (set) each time a complete SCC is found.

# New low-link update condition: If 'u' and 'v' are nodes in a graph and we're currently
# exploring 'u', then our new low-link update condition is that:
# To update the low-link value of node 'u' as equal to the low-link value of node 'v', there
# should be a path of edges from 'u' to 'v' and node 'v' must be on the stack!

# We can update the low-link values on-the-fly to obtain a linear time complexity of O(V + E)

# Tarjan's Strongly Connected Component Algorithm Overview:
#  * Mark the id of each node as unvisited
#  * Start DFS. Upon visiting a node, assign it an id and a low-link value (that is also the 
#    same as the node id). Also mark the current nodes as visited and add them to a seen stack.
#  * On completion of DFS recursive callback, if the previous node is on the stack, then min the 
#    current node's low-link value with the last node's low-link value. This allows low-link values 
#    to propogate throught the cycles in the graph!
#  * After visiting all neighbors, if the current node started a connected componene (if the node
#    is the origin/root node of the connected component in the order of the DFS traversal), then
#    pop nodes off stack until current node is rached! This removes all the nodes of the current
#    stringly-connected component from the stack (set) of valid node ids that can be used as 
#    low-link values!
#  * Continue the DFS from one of the remaining unvisited nodes.


"""

PSEUDOCODE FOR TARJAN'S STRONGLY CONNECTED COMPONENTS ALGORITHM:

UNVISITED = -1
n = number of nodes in the directed graph
g = adjacency list with directed edges

id = 0 # used to give each node an id
sccCount = 0 # used to count number of Strongly Connected Componentss found

# Index 'i' in these arrays represents node i
# Length n array to store ordered node ids and whether a node with particular id has been visited
ids = [0, 0, ..., 0]
# Length n array to store low-link values to corresponding nodes in 'ids'
low = [0, 0, ..., 0]
# Length n array of seen nodes that are part of the current main DFS call
onStack = [false, false, ..., false]
stack = an enmpty stack data structure with push and pop support for storing nodes of each SCC at once

function findSccs():
    # initialize all nodes as unvisited
    for (i = 0; i < n; i++): ids[i] = UNVISITED
    for (i = 0; i < n; i++):
        # perform new main dfs() call on unvisited nodes
        if ids[i] == UNVISITED:
            dfs(i)
    return low

function dfs(at):
    stack.push(at)
    onStack[at] = true
    ids[at] = low[at] = id++

    # Visit all neighbors and min low-link value on successful recursive callback
    for (to : g[at]):
        # recursively call dfs() on all the adjacent nodes of current node 'at' in the graph
        if (ids[to] == UNVISITED): dfs(to) # Recursive call
        # if the adjacent node of node 'at' is on the stack (set) of valid node ids, use it
        # to propogate and update the lowest low-link value across all the nodes of the
        # strongly connected component utilizing the recursive dfs() calls
        if (onStack[to]): low[at] = min(low[at], low[to])

        # After having visited all the neighbors of 'at', if we are at the start
        # node / origin node of the strongly connected component again in the recursive callstack, 
        # ie, if id(at) == low-link value(to), empty the 'onStack' seen nodes until we are back
        # to the start of the strongly connected component
        if (ids[at] == low[at]):
            for (node = stack.pop();;node = stack.pop()):
                # prevent the node of current strongly connected component from consideration for
                # low-link value of other SCCs
                onStack[node] = false
                # update the low-link values of all the nodes in the current strongly connect
                # component to be the root/origin node id
                low[node] = ids[at]
                # stop popping the 'stack' when we reach the root/origin node of the current SCC 
                # as the remaining nodes in the stack will be from other SCCs
                if (node == at): break
            # increment the number of SCCs found in the graph
            sccCount++
"""


# TARJAN'S STRONGLY CONNECTED COMPONENTS SOURCE CODE:


"""

/**
* An implementation of Tarjan's Strongly Connected Components Algorithm using 
* adjacency list of graph
*
* Time Complexity: O(V + E)
*/

import static java.lang.Math.min;
import java.util.*;

public class TarjanSccSolverAdjacencyList {
    
    private int n;
    private List<List<Integer>> graph;

    private boolean solved;
    private int sccCount, id;
    private boolean[] onStack;
    private int[] ids, low;
    private Dequeue<Integer> stack;

    private static final int UNVISITED = -1;

    public TarjanSccSolverAdjacencyList(List<List<Integer>> graph) {
        if (graph == null ||) throw new IllegalArgumentException("Graph cannot be null.");
        n = graph.size();
        this.graph = graph;
    } 

    // Returns the number of strongly connected components in the graph
    public int sccCount() {
        if (!solved) solve();
        return sccCount;
    }
    
    // Get the connected components of this graph. If two indexes have the same
    // value, then they are in the same SCC.
    public int[] getSccs() {
        if (!solved) solve();
        return low;
    }

    public void solve() {
        if (solved) return;

        ids = new int[n];
        low = new int[n];
        onStack = new boolean[n];
        stack = new ArrayDequeue<>();
        Arrays.fill(ids, UNVISITED);

        for (int i = 0; i < n; i++)
            if (ids[i] == UNVISITED)
                dfs(i);
        solved = true;
    }

    private void dfs(int at) {
        // Add the current node 'at' into the set of seen nodes 'stack'.
        stack.push(at);
        // mark the node 'at' to be present on the stack
        onStack[at] = true;
        ids[at] = low[at] == id++;

        for (int to : graph.get(at)) {
            if (ids[to] == UNVISITED) dfs(to); # Recursive call on unvisited 'to' nodes
            // propagate the lowest low-link value from all the neighbor 'to' nodes of node 'at'
            // from all the recursive calls of dfs() for the current strongly connected component
            if (onStack[to]) low[at] = min(low[at], low[to]);
        }

        // On recursive callback, if we are at the root node (start of SCC)
        // empty the seen stack until all nodes from the current SCC are removed
        // ie, until the root node of the SCC itself is removed from the stack.
        if (ids[at] == low[at]) {
            for (int node = stack.pop();;node = stack.pop()) {
                onStack[node] = false;
                low[node] = ids[at];
                if (node == at) break;
            }
            sccCount++;
        }
    }

    // Initialize adjacency list with 'n' nodes
    public static List<List<Integer>> createGraph(int n) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) graph.add(new ArrayList<>());
        return graph;
    }

    // Adds a directed edge from node 'from' to node 'to'
    public static void addEdge(List<List<Integer>> graph, int from, int to) {
        graph.get(from).add(to);
    }

    /* Example Usage */
    public static void main(String[] args) {
        int n = 8; // using an example graph with 8 nodes
        List<List<Integer>> graph = createGraph(n);

        addEdge(graph, 6, 0);
        addEdge(graph, 6, 2);
        addEdge(graph, 3, 4);
        addEdge(graph, 6, 4);
        addEdge(graph, 2, 0);
        addEdge(graph, 0, 1);
        addEdge(graph, 4, 5);
        addEdge(graph, 5, 6);
        addEdge(graph, 3, 7);
        addEdge(graph, 7, 5);
        addEdge(graph, 1, 2);
        addEdge(graph, 7, 3);
        addEdge(graph, 5, 0);

        TarjanSccSolverAdjacencyList solver = new TarjanSccSolverAdjacencyList(graph);
        
        // get the SCC label for each node in the order of nodes in the 'ids' array
        int[] sccs = solver.getSccs(); 
        // create a hash map for keeping tack of node indexes of each strongly connected component
        Map<Integer, List<Integer>> multimap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (!multimap.containsKey(sccs[i]))
                multimap.put(sccs[i], new ArrayList<>());
            multimap.get(sccs[i]).add[i];
        }

        // Prints:
        // Number of Strongly Connected Components: 3
        // Nodes: [0, 1, 2] from a Strongly Connected Component.
        // Nodes: [3, 7] from a Strongly Connected Component.
        // Nodes: [4, 5, 6] from a Strongly Connected Component.
        System.out.printf("Number of Strongly Connected Components: %d", solver.sccCount());
        for (List<Integer> scc : multimap.values()) {
            System.out.println("Nodes: " + scc + " form a Strongly Connected Component.");
        }
    }
}

"""





# TRAVELLING SALESMAN PROBLEM (TSP) WITH DYNAMIC PROGRAMMING (DP)

# Given a list of cities and the distances between each pair of cities, what is the shortest
# possible route that visits each city exactly once and returns to the origin city ? - TSP
# In other words, the problem is: given a complete graph with weighted edges (as an adjacency
# matrix), what is the Hamiltonial Cycle (path that visits every node once) of minimum cost ?

"""

            A   B   C   D                              3
        A   0   4   1   9                          A <---- B
                                                    \     /^  
        B   3   0   6   11         ==>               \  / 1
                                                      /\ 
        C   4   1   0   2                           /    \v 9
                                                   C <--- D
        D   6   5   -4  0                             -4


    One of the optimal tour consists of going from A -> D -> C -> B -> A
    The cost of this tour is 9 + (-4) + 1 + 3 = 9

"""

# NOTE: There can be many different tours of the graph nodes with the same minimum cost

# Finding the optimal solution to the TSP problem is very hard; in fact, the problem is 
# known to be NP-Complete. A problem is called NP (nondeterministic polynomial) if its 
# solution can be guessed and verified in polynomial time; nondeterministic means that no 
# particular rule is followed to make the guess. If a problem is NP and all other NP problems 
# are polynomial-time reducible to it, the problem is NP-complete.


# The brute force way to solve the TSP is to compute the cost of every possible tour.
# This means we have to try all possible permutations of node orderings which takes O(nPn) which
# is O(n!/(n - n)!)  = O(n!/0!) = O(n!) time.


"""

THE BRUTE FORCE APPROACH

            A   B   C   D                              Tour     Cost
        A   0   4   1   9                           ABDC        18
                                                    ABDC        15
        B   3   0   6   11                          ACBD        19
                                                    ACDB        11
        C   4   1   0   2                           ADBC        24
                                                   *ADCB        9
        D   6   5   -4  0                           BACD        11
                                                   *BADC        9
                                                    BCAD        24
                                                    BCDA        18
                                                    BDAC        19
                                                    BDCA        15
                                                    CABD        15
                                                    CADB        24
                                                   *CBAD        9
                                                    CBDA        19
                                                    CDAB        18
                                                    CDBA        11
                                                    DABC        18
                                                    DACB        19
                                                    DBAC        11
                                                    DBCA        24
                                                    DCAB        15
                                                   *DCBA        9


* incdicates possible solutions to the travelling salesman problem using the given graph adjacency
  matrix

"""

# The dynamic programing solution to the TSP significantly improves on the time complexity,
# taking it from O(n!) to O(n^2 * 2^n). At first glance, this may not seem like a substantial
# improvement, however, it now makes solving this problem feasible on graphs with up to 23 nodes
# on a typical computer.

"""

TSP with DP time complexity comparison

n       |        n!        |    (n^2 * 2^n)    |
--------|------------------|-------------------|
1       |        1         |          2        |
2       |        2         |          16       |
3       |        6         |          72       |
4       |        24        |          256      |
5       |        120       |          800      |
6       |        720       |          2304     |
...     |        ...       |          ...      |
15      |   1307674368000  |        7372800    |
16      |   20922789888000 |        16777216   |
17      |  355687428096000 |        37879808   |


O(n!) is great for small number of nodes < 10, but at 15 and above, we see a substantial improvement
in performance / efficiency with the DP approach with O(n^2 * 2^n) time complexity

"""

# Steps in TSP with DP:
# * The main idea in TSP with DP is to compute the optimal solution for all the subpaths of length
#   'N' while using information from the already known optimal partial tours of length 'N - 1'.
#   Before starting, make sure to select a node 0 <= 'S' <= 'N' to be the designated starting node
#   for the tour.
# * Next, compute and store the optimal value from 'S' to each node 'X' (!= 'S'). This will solve
#   TSP problem for all paths of length n = 2.
# * To compute the optimal solution for paths of length n = 3, we need to remember (store) two things
#   from each of the n = 2 cases:
#   1. The set of visited nodes in the subpath (The order of nodes visited in the n = 2 solutions)
#   2. The index of the last visited node in the subpath solution
#   Together, these two things form our dynamic programming state. There are 'N' possible nodes that
#   we could have visited last in the subpath solution and 2^N possible subsets of visited nodes for
#   n = 2. Therefore, the space needed to store the answer to each subproblem is bounded by O(N * 2^N). 
#   The best way to store the set of visited nodes is to use a single 32-bit integer in it binary 
#   representation, that acts as a bit field for each node in the graph (0 - unvisited, 1 - visited). 
#   A 32-bit integer in compact, quick and allows for easy caching in a memo table.
# * To solve n = 3, we're going to take the solved subpaths fron n = 2 and add another edge
#   extending to a node which has not already been visited from the last visited node (whose index 
#   has also been saved in our cache). This process continues iteratively until we complete solution
#   for n = N case.
# * To complete the TSP tour, we need to connect our tour back to the start node 'S'. Loop over the
#   end state in the memo table (where the binary representation of visited nodes is composed of all 
#   'N' bits as '1') for every possible end position and minimize the lookup value plus the cost of 
#   going back to 'S'.


"""

PSEUDOCODE FOR TRAVELLING SALESMAN PROBLEM SOLUTION USING DYNAMIC PROGRAMMING AND BIT MANIPULATION

# finds the minimum TSP tour cost
# m - 2D adjacency matrix representing the input graph
# S - index of the start node (0 <= S <= N)
function tsp(m, S):
    N = m.size

    # Initialize memo table 
    # Fill table with null values or infinity
    memo = 2D table of size (N x 2^N)

    setup(m, memo, S, N)
    solve(m, memo, S, N)
    minCost = findMinCost(m, memo, S, N)
    tour = findOptimalTour(m, memo, S, N)

    return (minCost, tour)
"""

