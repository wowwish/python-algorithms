# A Tree is an undirected Graph with no Cycles. Equivalently, each tree has is a connected Graph
# with N nodes and N-1 edges.

# Trees in the Wild: 
#   * Filesystem structures are inherently trees
#   * Social hierarchies
#   * Abstract Syntax Trees to decompose source code and mathematical expressions for easy evaluation
#   * Every webpage is a tree as an HTML DOM structure.
#   * The decision outcomes in game theory are often modeled as trees for ease of representation.
#   * Family trees
#   * File parsing/HTML/JSON/Syntax trees
#   * AVL trees, B-tree, red-black tree, segment trees, fenwick trees, treaps, suffix trees, tree maps/sets
#   * Probability trees
#   * Taxonomies

# STORING UNDIRECTED TREES:

# Start by labelling the tree nodes from [0, n)
# A very simple way of storing a tree is in the form of an edge-list. Edge list storage representation
# (which is super fast and easy to iterate over, but cannot efficiently query neighbours of a node):
"""

                [(0, 1),
                (1, 4),
                (4, 5),
                (4, 8),
                (1, 3),
                (3, 7),
                (3, 6),
                (2, 3),
                (6, 9),
                ]

"""
# A more popular option to store trees is in the form of an adjacency list (which allows querying
# neighbours of a node):
"""

                0 -> [1]
                1 -> [0, 3, 4]
                2 -> [3]
                3 -> [1, 2, 6, 7]
                4 -> [1, 5, 8]
                5 -> [4]
                6 -> [3, 9]
                7 -> [3]
                8 -> [4]
                9 -> [6]

"""
# You can also store a tree as an adjacency matrix but it is a hige waste of space and is normally not
# used.

# Rooted Trees are trees with a designated Root Node. Most rooted trees have directed edges which
# point away from the root node. However, it is also possible sometimes (rarely) to have trees where
# the edges point towards the root node. Generally, rooted trees are much easier to work with than
# undirected trees because of their well defined structures which allow easy recursive algorithms. 
# Related to rooted trees are Binary Trees which are trees for which every node has at most two child
# nodes.
# Related to the Binary Trees are the Binary Search Trees (BST) which are trees which are trees that
# satisfy the BST invariant which states that for every node x:
#           x.left.value (values in left sub-tree) < x.value < x.right.value (values in right sub-tree)


# STORING ROOTED TREES:

# Rooted Trees are naturally defined recursively in a top-down manner. In practice, you always maintain
# a pointer to the root node of the tree so that you can access the tree and its contents. Each node
# also has access to a list of all its children (called child nodes). All the leaf nodes (terminal nodes)
# of a tree donot have child nodes. Sometimes, it is also useful to maintain pointer to a node's parent
# node, effectively making edges bidirectional. However, this isn't usually neccessary because you can
# access a node's parent on a recursive function's callback.