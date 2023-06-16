# Unlike a list where all the elements are stored in contiguous memory locations, the nodes
# of a linked-list will be stored all over the place in heap memory

# Big O:
# Append to end - O(1)
# Pop from end - O(N) (a disadvantage compared to lists)
# Prepend to start - O(1) (an advantage over normal lists)
# Pop from start - O(1) (an advantage over normal lists)
# Insert - O(N)
# Remove - O(N)
# Lookup  by index- O(N) (a disadvantage over lists)
# Lookup by value - O(N)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # if the linked-list is empty
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # handling edge-case for when the linked-list had only one node which gets removed
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp # or you can also return temp.value for testing purposes
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        # If the linked-list is empty
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # handling additional edge-case where the linked list has only one Node which gets removed
        if self.length == 0:
            self.tail = None
        return temp      
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        # swap the head and tail. All the Nodes are still pointing in the forward direction.
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next # or can also be 'None' when using the for loop below
        for _ in range(self.length): # while after is not None:
            after = temp.next # this prevents potential errors in the last iteration
            temp.next = before
            before = temp
            temp = after
            
            


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.reverse()
my_linked_list.print_list()



# LC QUESTIONS


"""
1. Implement the find_middle_node method for the LinkedList class.
The find_middle_node method should return the middle node in the linked list WITHOUT using the length 
attribute.
If the linked list has an even number of nodes, return the first node of the second half of the list.
Keep in mind the following requirements:
  * The method should use a two-pointer approach, where one pointer (slow) moves one node at a time 
    and the other pointer (fast) moves two nodes at a time.
  * When the fast pointer reaches the end of the list or has no next node, the slow pointer should
    be at the middle node of the list.
  * The method should return the middle node or the first node of the second half of the list if 
    the list has an even number of nodes.
  * The method should only traverse the linked list once.  In other words, you can only use one loop.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        if self.head is None:
            return None
        fast = self.head
        slow = self.head
        while fast:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next
        return slow

"""
2. Write a method called has_loop that is part of the linked list class.
The method should be able to detect if there is a cycle or loop present in the linked list.
The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" 
algorithm, to determine the presence of a loop efficiently.
The method should follow these guidelines:
  * Create two pointers, slow and fast, both initially pointing to the head of the linked list.
  * Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves 
    two steps at a time.
  * If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this 
    occurs, the method should return True.
  * If the fast pointer reaches the end of the list or encounters a None value, it means there is no 
    loop in the list. In this case, the method should return False.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        if self.head is None:
            return False
        fast = self.head
        slow = self.head
        while fast:
            fast = fast.next
            if fast is not None:
                fast = fast.next
                slow = slow.next
                if fast == slow:
                    return True
        return False
    

"""
3. Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as 
input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.
Given this LinkedList:
  1 -> 2 -> 3 -> 4
If k=1 then return the first node from the end (the last node) which contains the value of 4.
If k=2 then return the second node from the end which contains the value of 3, etc.
If the linked list has fewer than k items, the program should return None.
The find_kth_from_end function should follow these requirements:
  * The function should utilize two pointers, slow and fast, initialized to the head of the linked list.
  * The fast pointer should move k nodes ahead in the list.
  * If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
  * The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
  * The function should return the slow pointer, which will be at the k-th position from the end of the list.
  * This is a separate function that is not a method within the LinkedList class. 
This means you need to indent the function all the way to the left. 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
def find_kth_from_end(linked_list, k):
    if linked_list.head is None:
        return None
    fast = linked_list.head
    slow = linked_list.head
    for _ in range(k - 1):
        fast = fast.next
        if fast is None:
            return None
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    return slow


"""
4. You are given a singly linked list and two integers m and n. Your task is to write a method 
reverse_between within the LinkedList class that reverses the nodes of the linked list from index 
m to index n (inclusive) in one pass and in-place.

Note: the Linked List does not have a tail which will make the implementation easier.

Input:
  * The method reverse_between takes two integer inputs m and n.
  * The method will only be passed valid indexes (you do not need to test whether the indexes are 
    out of bounds)

Output:
  * The method should modify the linked list in-place by reversing the nodes from index m to index n.
  * If the linked list is empty or has only one node, the method should return None.

Example:
  * Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4. Then, the method should 
    modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .

Constraints:
  * The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space 
    complexity of O(1).
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, m, n):
        if self.length <= 1:
            return
        # Create a dummy node and set it to point to self.head - This dummy node will help when the section of the linked-list
        # to be reversed starts from the head itself.
        dummy = Node(0)
        dummy.next = self.head
        front = dummy
        for _ in range(m):
            front = front.next # front is the node just before the start of the section to be reversed
        current = front.next # working node
        for _ in range(n - m):
            temp = current.next # node to be extracted (this becomes the next of the previous temp 
            # due to the below line of code)
            current.next = temp.next # extract the temp node by making current point to the next 
            # node after temp. This removes temp from the chain of links.
            temp.next = front.next # The extracted node should point to the frontmost node of 
            # the sublist that is being reversed (current is one Node before temp and is not the 
            # true starting node of the reversed sub-list)
            front.next = temp # Brings the extracted and processed Node to the front of the reversed 
            # sublist
        self.head = dummy.next # Update the head of the list if necessary


"""
5. You are given a singly linked list implementation in Python that does not have a tail pointer 
(which will make this method simpler to implement).

You are tasked with implementing a method partition_list(self, x) that will take an integer x and 
partition the linked list such that all nodes with values less than x come before nodes with values 
greater than or equal to x. You should preserve the original relative order of the nodes in each of 
the two partitions.

You need to implement this method as a method of the LinkedList class. The method should take an 
integer x as input. If the linked list is empty, the method should return None.

To implement this method, you should create two new linked lists. These two linked lists will be made 
up of the original nodes from the linked list that is being partitioned, one for nodes less than x and 
one for nodes greater than or equal to x. None of the nodes from the linked list should be duplicated.

The creation of a limited number of new nodes is allowed (e.g., dummy nodes to facilitate the 
partitioning process).
You should then traverse the original linked list and append each node to the appropriate new linked list.
Finally, you should connect the two new linked lists together.

Let's consider the list 2 -> 8 -> 1 -> 4 -> 3 -> 7, and we'll partition around the value 4.
Before:
    2 -> 8 -> 1 -> 4 -> 3 -> 7

After calling the partition_list(4), we have:
    2 -> 1 -> 3 -> 8 -> 4 -> 7

Explanation:
The partition_list method separates the nodes into two lists, one for nodes with values less than x 
and the other for nodes with values equal to or greater than x. The function then concatenates these 
two lists.
In the above example, the nodes with values less than 4 (i.e., 2, 1, and 3) come before the nodes with 
values equal to or greater than 4 (i.e., 8, 4, and 7). The relative order of the nodes is preserved.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x):
        if self.head is None:
            return None
        lesser = LinkedList(0)
        greater = LinkedList(0)
        current = self.head
        while current is not None:
            if current.value < x:
                lesser.append(current.value)
            elif current.value >= x:
                greater.append(current.value)
            current = current.next
        orig_current = self.head
        lesser_current = lesser.head.next
        while lesser_current is not None:
            orig_current.value = lesser_current.value
            orig_current = orig_current.next
            lesser_current = lesser_current.next
        greater_current = greater.head.next
        while greater_current is not None:
            orig_current.value = greater_current.value
            orig_current = orig_current.next
            greater_current = greater_current.next

    def partition_list2(self, x):
        if not self.head:
            return None
    
        dummy1 = Node(0) # The node which will be linked with nodes in self with value < x
        dummy2 = Node(0) # The node which will be linked with nodes in self with value >= x
        prev1 = dummy1
        prev2 = dummy2
        current = self.head # to traverse through self

        # traverse through nodes in self and link every node to corresponding node chain (dummy1 or 
        # dummy2) 
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
    
        prev1.next = None # terminate the chain of linked lists with nodes having value < x
        prev2.next = None # Terminate the chain of linked lists with nodes having value >= x
        prev1.next = dummy2.next # connect the two chain of linked lists in order
    
        self.head = dummy1.next # set self.head to point to the newly built, connected linked-list chain


"""
6. You are given a singly linked list that contains integer values, where some of these values may be 
duplicated.
Note: this linked list class does not have a tail which will make this method easier to implement.
Your task is to implement a method called remove_duplicates() within the LinkedList class that removes 
all duplicate values from the list.
Your method should not create a new list, but rather modify the existing list in-place, preserving the 
relative order of the nodes.

You can implement the remove_duplicates() method in two different ways:
    * Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes 
    in the linked list. You are allowed to use the provided Set data structure in your implementation.

    * Without using a Set - This approach will have a time complexity of O(n^2), where n is the number 
    of nodes in the linked list. You are not allowed to use any additional data structures for this 
    implementation.

Here is the method signature you need to implement:
    def remove_duplicates(self):

Example:

Input:
    LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
Output:
    LinkedList: 1 -> 2 -> 3 -> 4 -> 5
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next          

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    # O(N^2 solution)
    def remove_duplicates(self):
        outer_node = self.head
        while outer_node is not None:
            inner_node = outer_node.next
            while inner_node is not None:
                if inner_node.next.value == outer_node.value:
                    prev.next = inner_node.next
                    inner_node.next = None
                    inner_node = prev.next
                    self.length -= 1
                else:
                    inner_node = inner_node.next
                    prev = prev.next
            outer_node = outer_node.next

    # O(N) solution
    def remove_duplicates_optimized(self):
        unique_values = set()
        prev = None
        current_node = self.head
        while current_node is not None:
            if current_node.value in unique_values:
                prev.next = current_node.next
                current_node.next = None
                current_node = prev.next
                self.length -= 1
            else:
                unique_values.add(current_node.value)
                prev = current_node
                current_node = current_node.next


my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates_optimized()

my_linked_list.print_list()
