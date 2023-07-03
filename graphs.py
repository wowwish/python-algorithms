# A Graph consists of Vertices (Nodes) and Edges (connections between the Vertices or Nodes which can be
# unidirectional or bidirectional). The Edges can also have an associated weight which can be used
# for optimizing routes from one Vertex to another.

# Binary Trees are also a form of Graph with a limitation that each Vertex (or Node) can have connections 
# to only two other Vertices (or Nodes.). Similarly, linked-lists are also Graphs where a Vertex can
# have connection only one other Vertex.

# There are two ways of representing a Graph as a data structure:
#   * Adjacency Matrix - A matrix of 0s and 1s where the horizontal and vertical axis represent
#   all the Vertices of the Graph and a 1 denotes the presence of an Edge between the row and column 
#   vertices corresponding to the cell and a 0 denotes the absence of an Edge between the row and column
#   vertices corresponding to the matrix cell. The adjacency matrix of a Bidirectional Graph will be
#   a symmetric matrix.
# 
#   * Adjacency list - It is a dictionary where the key is a Vertex from the Graph and the value is
#   a list of all the Vertices to which this Vertex has Edges or connections to.


# SPACE COMPLEXITIES (V IS THE NUMBER OF VERTICES, E IS THE NUMBER OF EDGES)

# Adjacency List - has a space complexity of O(V + E) 
# Adjacency Matrix - has a space complexity of O(V^2)


# TIME COMPLEXITIES (V IS THE NUMBER OF VERTICES, E IS THE NUMBER OF EDGES)

# Adding a Vertex: Adjacency List- O(1), Adjacency Matrix - O(V^2)- have to update both row and column 
# with new Vertex
# Adding an Edge: Adjacency List - O(1), Adjacency Matrix - O(1)
# Removing an Edge: Adjacency List - O(E) - go through all edges in the list of the Vertex, Adjacency 
# Matrix - O(1)
# Removing a Vertex: Adjacency List - O(V + E) - remove the vertex from the dictionary and also remove
# all the edges pointing to that vertex from the other Vertices in the dictionary
# Removing a Vertex: Adjacency Matrix - O(V^2) - Remove the row and column corresponding to the Vertex.


# WE WILL BE USING AN ADJACENCY LIST TO REPRESENT OUR GRAHS BECAUSE OF THE SPACE EFFICIENCY.


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if (v1 in self.adj_list.keys()) and (v2 in self.adj_list.keys()):
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if (v1 in self.adj_list.keys()) and (v2 in self.adj_list.keys()):
            # The two vertices v1 and v2 may be present in the graph but may not be connected or have an
            # edge between them. In that case, we need to handle the exception that happens.
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass # ignore the exception caused due to no connection between the two vertices.
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            # This method can be made more efficient in the case of bi-directional graphs due to the
            # symmetric nature of the Edges or connections. We can use a for loop to get the other vertices
            # that the vertex to be removed from the Graph is connected to and easily remove the connections
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex] # remove the vertex itself from the adjacency list
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')

my_graph.remove_edge('A', 'D') # edge case handled by the try-except block. Notice that 'D' does not have
# any edge in the Graph.

my_graph.print_graph()