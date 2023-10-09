# LEAF NODE SUM - what is the sum of all the leaf node values in a tree ?


"""
PSEUDOCODE FOR LEAF NODE SUM

# Sums up leaf node values in a tree.
# Call function like: leafSum(root)

function leafSum(node):
    # Handle empty tree case
    if (node == null):
        return 0
    if isLeaf(node):
        return node.getValue()
    total = 0
    for child in node.getChildNodes():
        total += leafSum(Child) # Recursive call
    return total

function isLeaf(node):
    return node.getChildNodes.size() == 0
"""


# FIND THE HEIGHT OF A BINARY TREE - The height of a tree is the number of edges from root to lowest leaf node


"""
PSEUDOCODE FOR FINDING THE HEIGHT OF A BINARY TREE

# The height of a tree is the number of edges from
# the root to the lowest leaf.

function treeHeight(node):
    # Handle empty tree case
    if node == null:
        return -1
    
    # Identify leaf nodes and return zero (optional check)
    # The code will run just fine even without this case check.
    if (node.left == null) and (node.right == null):
        return 0
    
    return max(treeHeight(node.left), treeHeight(node.right)) + 1 # Recursion
"""


# ROOTING A UNDIRECTED TREE (GRAPH) - adds structure to the problem you are solving

# An example of an undirected tree is:
"""
0 -> [2, 1, 5],
1 -> [0],
2 -> [3, 0],
3 -> [2],
4 -> [5],
5 -> [4, 6, 0],
6 -> [5],
"""

# Conceptually, rooting a tree is like "picking up" the tree by a specific node and having
# all the edges point downwards. You can root a tree using any of its nodes, However, be
# cautious, because not every node you select will result in a well balanced tree. Hence,
# you need to be selective if this is your objective.
# In some situations, it is also useful to have a reference to the parent node at each node,
# in order to be able to walk up the tree.
# Rooting a tree is easily done depth first.

"""
PSEUDOCODE FOR ROOTING A TREE

# The Algorithm starts on the designated root node.

# TreeNode object structure used to store a node of the tree.
class TreeNode:
    # unique integer id to identify this node
    int id;

    # Pointer to parent TreeNode reference. Only the 
    # root node has a null parent TreeNode reference.
    TreeNode parent;

    # List of pointers to child TreeNodes.
    TreeNode[] children;

# g is the graph/tree represented as an adjacency list
# with undirected edges. If there's an edge between (u, v)
# there's also an edge between (v, u). rootId is the id of
# the node to root the tree from.
function rootTree(g, rootId = 0):
    root = TreeNode(rootId, null, [])
    return buildTree(g, root, null)

# Build tree recursively depth first.
function buildTree(g, node, parent):
    for childId in g[node.id]:
        # Avoid adding an edge pointing back to the parent
        if (parent != null) and (childId == parent.id):
            continue
        child = TreeNode(childId, node, [])
        node.children.add(child)
        buildTree(g, child, node)
        return node
"""


# FINDING CENTER(S) OF A TREE - handy for finding the root node to root our
# undirected tree

# Note that there could be more than one centre(s) to a tree.
# Notice that the centre is always the middle vertex or middle two vertices in
# every longest path along the tree.
# Another approach to finding the center is to iteratively pick off each leaf
# node layer like we are peeling an onion. Keep in mind that leaf nodes have
# a degree of 1. With each iterative step, you can prune the nodes with degree
# 1 and then update the degree of the remaining nodes until you left with either
# one or two nodes.

"""
PSEUDOCODE FOR FINDING TREE CENTER

# g = tree represented as an undirected graph with nodes named with number
function treeCenters(g):
    n = g.numberOfNodes()
    degree = [0, 0, ..., 0] # size n
    leaves = []
    for (i = 0; i < n; i++):
        degree[i] = g[i].size()
        if degree[i] == 0 or degree[i] ==1:
            leaves.add(i)
            degree[i] = 0
    count = leaves.size()
    while (count < n): # while number of leaves not equal to number of nodes
        new_leaves = []
        for (node: leaves):
            for (neighbor: g[node]):
                degree[neighbor] = degree[neighbor] - 1
                if degree[neighbor] == 1:
                    new_leaves.add(neighbor)
            degree[node] = 0
        count += new_leaves.size() # increment count with leaves in current layer
        leaves = new_leaves
    return new_leaves # center(s)
"""


# ISOMORPHISMS IN TREES - A QUESTION OF TREE EQUALITY

# A question of asking whether two graphs G1 and G2 are isomorphic is asking
# whether they are "structurally" the same (same number of vertices and same
# number as well as node pair of edge connections when the vertices are
# relabelled).
# In simple terms, for an isomorphism to exist, there needs to be a
# (bijection) function "phi" which can map all the nodes/edges in G1
# to G2 and vice-versa.

# Determining if two graphs are isomorphic is not only not obvious to the human eye,
# but also a difficult problem to solve for computers. It is still an open question
# as to whether the graph isomorphism problem is NP complete. However, many polynomial
# time isomorphism algorithms exist for graph sub-classes such as trees.


"""
NON-ISOMORPHIC TREES:

          TREE 1                          TREE 2
            0                               3
            |                               |
            |                               |
            1                               4
            |                           0  /|
            |                           | / |
            2                           |/  5
           /|\                          1
          / | \                         | 
         /  4  \                        |
        3       5                       2


                
ISOMORPHIC TREES:

        TREE 1                            TREE 2

   6    0 ------ 1                         1
    \   |                                  |
      \ |                             0    |
        2                              \   2
      / |                               \  |
    /   |                                \ |
   3    5                                  3 ------ 4
   |                                       |
   |                                       |
   4                              6 ------ 5
        
        
ONE POSSIBLE LABEL MAPPING (TREE1->TREE2): 2->3, 0->5, 1->6, 5->4, 3->2, 4->1, 6->0
"""


# There are several very quick "probabilistic" (usually hash or heuristic based) algorithms for
# identifying isomorphic trees. These tend to be fast, but are also error prone due to hash collisions
# in a limited integer space.
# The method we will look at will "serialize" a tree into a unique encoding. This unique encoding is
# simply a unique string that represents the tree. If another tree has the same encoding, then, they
# are isomorphic.
# We can directly serialize na unrooted tree, but in practice, serializing a rooted tree is typically
# easier to code. One caveat to watch out for if we're going to serialize out two isomorphic
# trees, is to make sure that both the trees are rooted using the same isomorphic node before serializing
# the trees.
# To select a common node that is isomorphic between the two trees, we can find the centers of both the trees
# and use the respective centers to root the trees. AAfter finding the center(s) of both trees, then root
# the trees at their center node, then generate the encoding for each tree and compare the serialized
# trees for equality.
# In our case, the tree encoding will simply be a sequence of left '(' and rigt ')' brackets. However,
# you can also think of them as 1's and 0's (ie, a large number) if you prefer. It is also possible
# to reconstruct the original tree from this encoding.

# The AHU (Aho, Hopcroft, Ullman) algorithm is a clever serialization technique for representing a
# tree as a unique string. Unlike many tree isomorphism invariants and heuristics, AHU is able to
# capture a "complete history" of a tree's "degree spectrum" and structure, ensuring a deterministic
# method of checking for tree isomorphisms.

# TREE ENCODING:
# * all leaf nodes are assigned knuth tuples '()'
# * next, all the parents of the leaf nodes will be assigned with the combined labels of their children
#   wrapped in brackets
# * continue this process of wrapping child labels for all parents higher up the tree.
#   The child labels need to be sorted in an order (left-child label first, then right-child or right-child
#   label first, then left child orlexicographic sorting) when combining. This ensures uniqueness of the parent 
#   label within the tree. You cannot process a node until all its children are processed.

"""
TREE ENCODING

                             '(((())())(()())(()))'
                                        0
                                      / | \
                                     /  |  \
                                    /   |   \
                                   /    |    \
                            '((())())'  1     3 '(())'
                                 /     /|      \
                                /     / |       \
                               /     /  |        \
                              /     /   |         \
                             /     4    5 '(())'   8
                            /    '()'   |         '()'
                 '(()())'  2            |
                         /  \           |
                        /    \          |
                       /      \         9
                      6        7       '()'
                    '()'      '()'

"""


"""

PSEUDOCODE FOR UNROOTED TREE ENCODING:

# Returns whether two trees are Isomorphic
# Parameters tree1 and tree2 are undirected trees
# stored as adjacency lists
function treesAreIsomorphic(tree1, tree2):
    tree1_centers = treeCenters(tree1)
    tree2_centers = treeCenters(tree2)

    tree1_rooted = rootTree(tree1, tree1_centers[0]) # using only the first center in this case
    tree1_encoded = encode(tree1_rooted)

    # Go through each centre of tree2, get it rooted at the center
    # and encode the centred tree. Then, compare the encoding with tree1's encoding
    for center in tree2_centers:
        tree2_rooted = rootTree(tree2, center)
        tree2_encoded = encode(tree2_rooted)
        # Two trees are isomorphic if their encoded
        # canonical forms are equal
        if tree1_encoded == tree2_encoded:
            return True
    return False

function encode(node):
    if node == null:
        return ""

    labels = []
    for child in node.children:
        labels.add(encode(child))

    # Regular Lexicographic Sort
    sort(labels)

    result = ""
    for label in labels:
        result += label
    return "(" + result + ")"
"""

# In this case, the Rooted Trees are stored as Recursive TreeNode objects:

"""
# TreeNode object structure
class TreeNode:
    # unique integer id to identify this node
    int id;

    # pointer to parent TreeNode reference. Only the root TreeNode has
    # a null parent TreeNode reference
    TreeNode parent;

    # list of pointers to child TreeNodes
    TreeNode[] children;
"""
