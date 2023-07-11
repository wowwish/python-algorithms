# A MaxHeap is a Binary Tree where each Node has a value that is higher than all of its descendants.
# A MinHeap is a Binary Tree where each Node has a value that is lower than all of its descendants.
# Hence, in a MaxHeap, the root will always have the highest value, and in a MinHeap, the root
# will always have the lowest value.
# However, unlike Binary Search Trees, a Heap cannot be used for Searching as it does not maintain
# proper order. The second highest value can be the left-child of the root, right-child of the root
# or it can also be at the third level of the Binary Tree in a MaxHeap.
"""
The Following are all valid MaxHeaps:

        99
       /  \
      72   61
    /  \  /  \ 
   58  55 27  18

        99
       /  \
      61   72
    /  \  /  \ 
   58  55 27  18

        99
       /  \
      72   58
    /  \  /  \ 
   55  61 27  18
         ______________________                        ________________________ 
0-based: |99|72|61|58|55|27|18|               1-based: |x|99|72|61|58|55|27|18|
          0  1  2  3  4  5  6                           0  1  2  3  4  5  6  7
"""
# Because of this, a Heap is stored as an array or a list of integers instead of a bunch of connected 
# Nodes that is used to store Trees. The Heap can be stored from index 0 or index 1 of the array/list.
# The filling up of the list/array for a Heap follows the left-child-then-right-child order.
# Hence, for a Heap filled from index 1,
#   index of left child = 2 * parent index
#   index of right child = 2 * parent index + 1
#   parent index = int(child inded / 2)
# A Heap is a Complete Tree (Every Node will be filled from the left-child-to-right-child direction 
# and the higher levels will be filled first before the lower levels of the tree).
# The height of a heap will be logN where N is the number of nodes.
# While a normal tree does not allow duplicate values, a Heap can have Nodes with duplicate values.

# Heaps are used to build an efficient Priority Queue where the Maximum Priority value is always
# the first element of the Heap. Maximum Prioirty could mean the highest value or the lowest value and
# the MinHeap of MaxHeap can be used depending on the situation.

# Heap Space Complexity: O(N)
# Heap Time Complexity for Insert and Remove: O(logN)


# A 0-index based MaxHeap
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2 # integer division
    
    def swap(self, index1, index2): # swap values at two indices
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        # Bubbling Up the inserted value to its corresponding index in the MaxHeap
        while (current > 0) and (self.heap[current] > self.heap[self._parent(current)]):
            self.swap(current, self._parent(current))
            current = self._parent(current)
    
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            # get the index of the child with the highest value
            if (left_index < len(self.heap)) and (self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            if (right_index < len(self.heap)) and (self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            if max_index != index:
                self.swap(index, max_index) # sink-down the value to the left or right child depending on max_index
                index = max_index # update index to calculate new left_index and right_index in next iteration
            else: # To terminate the while loop and prevent infinite loop
                return

    def remove(self): 
        # We always remove only the root element from the heap
        # We then take the right-most leaf node an put it in place of the root
        # Then we perform the sink-down operation on the new root
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0] # root value
        self.heap[0] = self.heap.pop() # replace root with the right-most leaf node
        self._sink_down(0) # put the new root value to its corresponding postion in the MaxHeap
        return max_value


my_heap = MaxHeap()
my_heap.insert(95)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)

print(my_heap.heap)

my_heap.remove()
print(my_heap.heap)
my_heap.remove()
print(my_heap.heap)