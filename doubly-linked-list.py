class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        mid = int(self.length / 2)
        if mid < index:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
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
        before = self.get(index - 1)
        after = before.next

        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp
    

my_double_linked_list = DoublyLinkedList(0)
my_double_linked_list.append(1)
my_double_linked_list.append(2)
print(my_double_linked_list.remove(1).value, '\n')
my_double_linked_list.print_list()




# LC QUESTIONS


"""
1. Swap the values of the first and last node

Method name:
swap_first_last

Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def swap_first_last(self):
        if self.length == 0:
            return
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
        # or alternatively: self.head.value, self.tail.value = self.tail.value, self.head.value

    
    
"""
2. Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first 
node becomes the last node, the second node becomes the second-to-last node, and so on.

To do this, you'll need to traverse the list and change the direction of the pointers between the nodes 
so that they point in the opposite direction.

Do not change the value of any of the nodes.

Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect 
the new order of the nodes.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        

    def reverse(self):
        if self.head is None:
            return 
        current = self.head
        self.head = self.tail
        self.tail = current
        while current is not None:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp


"""
3. Write a method to determine whether a given doubly linked list reads the same forwards and backwards.

For example, if the list contains the values [1, 2, 3, 2, 1], then the method should return True, since 
the list is a palindrome.

If the list contains the values [1, 2, 3, 4, 5], then the method should return False, since the list 
is not a palindrome.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def is_palindrome(self):
        if self.length <= 1:
            return True
        mid = self.length/2 
        index = 0
        forward = self.head
        backward = self.tail
        while index <= mid:
            if forward.value == backward.value:
                forward = forward.next
                backward = backward.prev
                index += 1
            else:
                return False
        return True
    

"""
4. You are given a doubly linked list.
Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the 
linked list. The method should not take any input parameters.
Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

Example:

    1-->2-->3-->4--> should become 2-->1-->4-->3-->

Your implementation should handle edge cases such as an empty linked list or a linked list with only 
one node.
Note: You must solve the problem without modifying the values in the list's nodes (i.e., only the 
node's prev and next pointers may be changed.)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        # handle edge-cases
        if self.length <= 1:
            return
        first = self.head
        second = first.next
        self.head = self.head.next # correct the head beforehand
        # handle the first pair seperately and then loop over the remaining pairs
        second.prev = first.prev
        first.prev = second
        first.next = second.next
        second.next = first
        # Check for presence of a pair and terminate the loop when there is no pair or when only 
        # a single node if left
        while (first.next is not None) and (first.next.next is not None):
            print('Iterated!')
            # move to the next pair 
            first = first.next
            second = first.next
        
            # Connect previous reversed pair with current pair
            first.prev.next.next = second
            first.prev = first.prev.next

            # Reverse the pair to which we currently moved
            second.prev = first.prev
            first.prev = second
            first.next = second.next
            second.next = first

    def swap_pairs2(self):
        # Create a dummy node to simplify swapping logic
        dummy = Node(0)
        # Connect the dummy node to the head of the list
        dummy.next = self.head
        # Set 'prev' to the dummy node for the first iteration
        prev = dummy
    
        # Iterate while there are at least two nodes left
        while self.head and self.head.next:
            # Identify the first node of the pair to swap
            first_node = self.head
            # Identify the second node of the pair to swap
            second_node = self.head.next
    
            # Update 'next' pointers to swap the node pair
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
    
            # Update 'prev' pointers for the swapped nodes
            second_node.prev = prev
            first_node.prev = second_node
            # Set the 'prev' of the node after the pair
            if first_node.next:
                first_node.next.prev = first_node
    
            # Move 'head' to the next pair of nodes
            self.head = first_node.next
            # Update 'prev' to the last node in the pair
            prev = first_node
 
        # Set the new head of the list after swapping
        self.head = dummy.next
        # Ensure the new head's 'prev' does not point to dummy
        if self.head:
            self.head.prev = None

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()
