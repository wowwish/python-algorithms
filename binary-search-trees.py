# A linked-list is a form of a tree that does not fork.
# Every node in a tree can be a Parent and a child, except for the root which cannot have a Parent
# and the terminal (or leaf) nodes which cannot have a Child.
# In a Binary tree, every Parent can have a maximum of two Children (the two Child nodes of a Parent are
# also called as Sibling nodes and are referenced by left and right pointers).
# Similarly, in a Binary Search Tree, a node can have a maximum of one Parent.
# In a Full Binary Tree, every node points to either zero nodes or two nodes.
# In a Perfect Binary Tree, every node in every level of the Binary Tree has two children, except
# the terminal child nodes.
# A Complete Binary Tree will be filled from left to right, ie, the nodes in a level are filled from
# left-right direction ie, for a node in a given level, its left child is filled first, followed by its 
# right child with nodes in higher levels being filled first before the nodes in the lower levels.

# A Binary Search Tree (BST) is a Binary Tree where the left Child should have a value less than the
# Parent node and the right Child should have a value greater than the Parent node. For a given node
# in the BST, all nodes in its left branch will have values lesser than its own value and all nodes in 
# its right branch will have values greater than its own value.

# WE GENERALLY CONSIDER THE BIG-O FOR LOOKUP, INSERT AND REMOVE IN BINARY SEARCH TREE AS O(logN).
# HOWEVER, AN EXCEPTION TO THIS ASSUMPTION IS A BST WHERE EVERY PARENT HAS ONLY ONE CHILD WHICH IS
# EITHER GREATER THAN IT AND TO THE RIGHT OR LESSER THAN IT AND TO THE LEFT (SIMILAR TO A LINKED-LIST).
# INSERT, LOOKUP AND REMOVE IN SUCH A BST WILL HAVE A BIG-O OF O(N) - WORST CASE.

# A BST is better in terms of time-complexity for lookup and removal. However, a linked-list is 
# more efficient than a BST for insertion.

# A BST can be traversed breadth-first (visit all nodes in a level and then descend to the next level)
# or depth-first (move to left-most leaf node from the root and then backtrack to the last visited node
# at the lowemost level and continue tracing paths towards leaf nodes). The depth-first traversal can be done
# in three orders: 
#   * pre-order DFS  - parent node first, left next, then right node
#   * post-order DFS - left first, next right, then the parent node
#   * in-orderDFS - left first, then the parent node, then right node

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def recursive_insert(self, value):
        def helper(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = helper(node.left, value)
            if value > node.value:
                node.right = helper(node.right, value)
            return node

        if self.root is None:
            self.root = Node(value)
        helper(self.root, value)
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value: return False # handling edge-case of value to be inserted being same as the current node value
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self, value):
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            elif value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
        return False

    def recursive_contains(self, value):
        def helper(node, value):
            if node is None:
                return False
            if value == node.value:
                return True
            elif value > node.value:
                return helper(node.right, value) # recursive call
            elif value < node.value:
                return helper(node.left, value) # recursive call
            
        return helper(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            # insert into the left sub-tree when the value to be inserted < current_node.value
            current_node.left = self.__r_insert(current_node.left, value) # recursive call
        if value > current_node.value:
            # insert into the right sub-tree when the value to be inserted > current_node.value
            current_node.right = self.__r_insert(current_node.right, value) # recursive call
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    # A method to find the mim=nimum value in the sub-tree of of a given node
    def minimum_value(self, node):
            while(node.left is not None):
                node = node.left
            return node.value # returns the input node's value itself when the input node does not have
            # any left child

    # helper function to delete a node
    def __delete_node(self, current_node, value): 
        if current_node is None: # base-case or termination condition for recursion
            # If we reach here, either the value is not present in the BST or the tree is empty.
            # In either case, we need to return None which will be set as the modified sub-tree after
            # deletion in a particular side of a node of the tree.
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else: # we reach the else condition only when value == current_node.value
            # edge-case of deleting a leaf node with no children - we return None, making the new
            # current node as None, deleting the current node passed to this method call.
            if (current_node.left is None) and (current_node.right is None):
                return None
            # edge-case of deleting a node with only a right child - make the right child of the current 
            # node as the current node itself, deleting the current node passed to this method call.
            elif (current_node.left is None):
                current_node = current_node.right
            # edge-case of deleting a node with only a left child - make the left child node of the
            # current node as the current node itself, deleting the current node passed to this method call.
            elif (current_node.right is None):
                current_node = current_node.left
            # edge-case of deleting a node with both children - we find the minimum (left-most leaf node)
            # in the right sub-tree of the passed current node and set it as the value of the current 
            # node passed to this method. Then, we delete that left-most leaf node (minimum value of
            # the right sub-tree of the current node) and delete that leaf node.
            else:
                sub_tree_min = self.minimum_value(current_node.right)
                current_node.value = sub_tree_min
                # recursive call to delete the leaf node with the minimum value in the right sub-tree
                # of the current node passed to this method call.
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

        return current_node
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    # Breadth-First Search Traversal of the tree using a queue (FIFO) for help
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while (len(queue) > 0):
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
            
    def dfs_pre_order(self):
        results = []
        def traverse_helper(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse_helper(current_node.left) # recursive call
            if current_node.right is not None:
                traverse_helper(current_node.right) # recursive call
        traverse_helper(self.root)
        return results

    def dfs_post_order(self):
        results = []
        def traverse_helper(current_node):
            if current_node.left is not None:
                traverse_helper(current_node.left) # recursive call
            if current_node.right is not None:
                traverse_helper(current_node.right) # recursive call
            results.append(current_node.value)
        traverse_helper(self.root)
        return results

    def dfs_in_order(self):
        results = []
        def traverse_helper(current_node):
            if current_node.left is not None:
                traverse_helper(current_node.left) # recursive call
            results.append(current_node.value)
            if current_node.right is not None:
                traverse_helper(current_node.right) # recursive call
        traverse_helper(self.root)
        return results

my_tree = BinarySearchTree()
my_tree.recursive_insert(47)
my_tree.recursive_insert(21)
my_tree.recursive_insert(76)
my_tree.recursive_insert(18)
my_tree.recursive_insert(27)
my_tree.recursive_insert(52)
my_tree.recursive_insert(82)
# my_tree.delete_node(21)

# print(my_tree.root.value)
# print(my_tree.root.left.value)
# print(my_tree.root.right.value)
# print(my_tree.root.left.left.value)
# print(my_tree.root.left.right)
# print(my_tree.root.right.left.value)
# print(my_tree.root.right.right.value)
# print(my_tree.recursive_contains(82))
print(my_tree.BFS())
print(my_tree.dfs_in_order())





# LC QUESTIONS



"""
1. You are tasked with writing a method called is_valid_bst in the BinarySearchTree class that checks 
whether a binary search tree is a valid binary search tree.
Your method should use the dfs_in_order method to get the node values of the binary search tree in 
ascending order, and then check whether each node value is greater than the previous node value.
If the node values are not sorted in ascending order, the method should return False, indicating that 
the binary search tree is not valid.
If all node values are sorted in ascending order, the method should return True, indicating that the 
binary search tree is a valid binary search tree.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) 
            if current_node.right is not None:
                traverse(current_node.right)          
        traverse(self.root)
        return results
        
    def is_valid_bst(self):
        result = self.dfs_in_order()
        for i in range(1, len(result)):
            if result[i - 1] > result[i]:
                return False
        return True
    


"""
2. Given a binary search tree, find the kth smallest element in the tree. For example, if the tree 
contains the elements [1, 2, 3, 4, 5], the 3rd smallest element would be 3.
The solution to this problem usually involves traversing the tree in-order (left, root, right) and 
keeping track of the number of nodes visited until you find the kth smallest element. There are two 
main approaches to doing this:

Iterative approach using a stack: This approach involves maintaining a stack of nodes that still need 
to be visited, starting with the leftmost node. At each step, you pop a node off the stack, decrement 
the kth smallest counter, and check whether you have found the kth smallest element. If you have not, 
you continue traversing the tree by moving to the right child of the current node.

Recursive approach: This approach involves recursively traversing the tree in-order and keeping track 
of the number of nodes visited until you find the kth smallest element. You can use a helper function 
that takes a node and a value of k as input, and recursively calls itself on the left and right 
children of the node until it finds the kth smallest element.

Both of these approaches have their own advantages and disadvantages, and the best approach to use may 
depend on the specific problem constraints and the interviewer's preferences.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    
    def kth_smallest(self, k):
        stack = []
        node = self.root
        while stack or node:
            # traverse to the left-most leaf node and start from there
            while node:
                stack.append(node)
                node = node.left
            # start from the leftmost leaf node and then
            # keep going to the parent using the stack in subsequent iterations
            node = stack.pop()
            k -= 1
            if k == 0: # When the k-th node is reached, return its value
                return node.value
            node = node.right # once the left node is checked,
            # check the right node in the next iteration before going to the parent
        return None # return None when k > number of nodes in tree

