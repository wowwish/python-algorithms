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




# A 0-index based MinHeap Implementation
class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        min_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            
            if (left_index < len(self.heap)) and (self.heap[left_index] < self.heap[min_index]):
                min_index = left_index
           
            if (right_index < len(self.heap)) and (self.heap[right_index] < self.heap[min_index]):
                min_index = right_index
            
            if min_index != index:
                self._swap(index, min_index)
                index = min_index
            else:
                return
    

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return min_value
        
        
        
myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]





# LC QUESTIONS


"""
1. You are given a list of numbers called nums and a number k. Your task is to write a 
function find_kth_smallest(nums, k) to find the kth smallest number in the list. 
The list can contain duplicate numbers and k is guaranteed to be within the range of the 
length of the list.
This function will take the following parameters:
        nums: A list of integers.
        k: An integer.

This function should return the kth smallest number in nums.

Example 1:
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        print(find_kth_smallest(nums, k))
        In the example above, the function should return 2. If we sort the list, it becomes 
        [1, 2, 3, 4, 5, 6]. The 2nd smallest number is 2, so the function returns 2.


Example 2:
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        print(find_kth_smallest(nums, k))
        In the example above, the function should return 3. If we sort the list, it becomes 
        [1, 2, 2, 3, 3, 4, 5, 5, 6]. The 4th smallest number is 3, so the function returns 3.

Note: For the purpose of this problem, we assume that duplicate numbers are counted as separate 
numbers. For example, in the second example above, the two 2s are counted as the 2nd and 3rd smallest 
numbers, and the two 3s are counted as the 4th and 5th smallest numbers.
Please write your solution in Python and use a max heap data structure to solve this problem. 
The MaxHeap class is provided for you.
Note: This is a separate function, not a method in the MaxHeap class so you will need to indent all 
the way to the left.
"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value



def find_kth_smallest(nums, k):
    mh = MaxHeap()
    for n in nums:
        mh.insert(n)
    for _ in range(len(nums) - k + 1):
        smallest = mh.remove()
    return smallest


"""
2. Write a function named stream_max that takes as its input a list of integers (nums). 
The function should return a list of the same length, where each element in the output list 
is the maximum number seen so far in the input list.
More specifically, for each index i in the input list, the element at the same index in the 
output list should be the maximum value among the elements at indices 0 through i in the input list.
Use the provided MaxHeap class to solve this problem. You should not need to modify the MaxHeap 
class to complete this task.

Function Signature: def stream_max(nums):

Examples:

        If the input list is [1, 3, 2, 5, 4], the function should return [1, 3, 3, 5, 5].
        Explanation:
                At index 0, the maximum number seen so far is 1.
                At index 1, the maximum number seen so far is 3.
                At index 2, the maximum number seen so far is still 3.
                At index 3, the maximum number seen so far is 5.
                At index 4, the maximum number seen so far is still 5.
                So, the output list is [1, 3, 3, 5, 5].
        
        Similarly, if the input list is [7, 2, 4, 6, 1], the function should return [7, 7, 7, 7, 7].
        Explanation:
                At each index, the maximum number seen so far is 7.
                So, the output list is [7, 7, 7, 7, 7].

Constraints:
You may assume that the input list does not contain any null or undefined elements.
"""

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
        


def stream_max(nums):
    mh = MaxHeap()
    result = []
    for n in nums:
        mh.insert(n)
        result.append(mh.heap[0])
    return result

