# BUBBLE SORT - keep swapping the elements of input list, moving the greatest element to the last with each swap. Repeat the swapping
# rounds excluding the last element of the previous round (which will be placed in its correct position). This version of Bubble sort
# sorts the input array in ascending order.

def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1): # loop in reverse through the indices of the input list
        for j in range(i):
            # swapping condition
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

print(bubble_sort([2, 3, 1, 4, 5]))



# SELECTION SORT - keep track of the index of the minium value with every iteration within the array and swap the minimum value using this
# index to the start index of every iteration. This start index approaches the end of the array with every iteration. This version of
# Selection sort also sorts the input array in ascending order.

def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        # swap only when necessary
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print(selection_sort([6, 2, 3, 1, 4, 5]))



# INSERTION SORT - usually we start from the second item in the list and compare it to the first element and swap the first and second
# if the second element is less than the first element. In the next iteration, we would potentially compare the third element with the 
# second, swap if necessary and then the swapped third element with the first element and perform swap if necessary again. In the next
# iteration, the fourth element would be potentially compared and swapped with the third and then second and then the first element.
# At the end of all iterations, we have a ascending order sorted list. We can optimize the number of comparisons by stopping when the
# previous element is less than the current element.

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i] # current element to be inserted in its correct position in the ascending order of sorted elements.
        j = i - 1 # j is used to keep track of the previous elements of temp which are > temp and must be swapped with it.
        while (temp < my_list[j]) and (j > -1): # while loop is used to optimize for the number of comparisons and also to prevent index errors
            # swap and decrement j (the index of element to be compared with temp)
            my_list[j+1] = my_list[j] # i = j + 1 for first iteration
            my_list[j] = temp
            j -= 1
    return my_list

print(insertion_sort([6, 2, 3, 1, 7, 5, 4]))


# BUBBLE, SELECTION AND INSERTION SORT ALL HAVE A TIME COMPLEXITY OF O(N^2) AND SPACE COMPLEXITY OF O(1)
# IF YOU START WITH A PRE-SORTED (OR ALMOST SORTED) ARRAY, INSERTION SORT WILL HAVE A TIME COMPLEXITY OF O(N) BECAUSE OF ITS OPTIMIZATION
# WHEREAS BUBBLE AND SELECTION SORT WILL STILL HAVE O(N^2) TIME COMPLEXITY!









# MERGE SORT - use a recursive divide and conquer approach to split the input list into single element
# lists which are always sorted becuase they contain only one element. Use a merge function to merge
# these sorted sub-lists to generate the final sorted list.

# REMEMBER THAT MERGE SORT CREATES A NEW SORTED LIST WHILE THE ORIGINAL LIST REMAINS INTACT
# Space Complexity: O(N)
# Time Complexity: O(N . logN)

# Helper function to merge two sorted sub-lists
def merge(list1, list2):
    combined = []
    i = 0 # index for first sub-list
    j = 0 # index for second sub-list
    while(i < len(list1) and j < len(list2)): # This loop runs only till one of the input list is exhausted
        # we have to add items left-over in the other list after this loop ends to the result.
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    # Add left-over items from sub-list 1 if any to the result
    while(i < len(list1)):
        combined.append(list1[i])
        i += 1
    # Add left-over items from sub-list 2 if any to the result
    while(j < len(list2)):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    # base-case or termination condition for the recursion
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    # split the input list at the middle
    left = merge_sort(my_list[:mid_index]) # recursive call on left sub-list
    right = merge_sort(my_list[mid_index:]) # recursive call on right sub-list
    return merge(left, right)


original_list = [3, 1, 4, 2]
sorted_list = merge_sort(original_list)
print('Original list:', original_list)
print('Sorted list:', sorted_list)










# QUICK SORT
# pick a pivot element (usually the first eleent of the input list) and then compare all other elements
# from the input list and swap elements smaller than the pivot with the first element greater than
# the pivot, found in the current iteration. Now, the input list will have the pivot with all the elements
# greater than the pivot together and all elements less than the pivot together. Finally, swap the
# pivot element with with the last of the element that was found to be less than the pivot. 
# These steps are now recursively performed on the sub-list to the left of the pivot which are the group of
# elements which are less than the pivot, and also on the sub-list to the right of the pivot which are
# the group of elements which are greater than the pivot. 

# Space Complexity: O(1) - quick sort is an in-place sorting algorithm
# Time Complexity: O(N . logN) in average case and O(N^2) for already sorted data (worst case)


def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, left, right):
    if right <= left:
        return my_list
    pivot_index = pivot(my_list, left, right)
    quick_sort_helper(my_list, left, pivot_index - 1) # recursive call on the left sub-list
    quick_sort_helper(my_list, pivot_index + 1, right) # recursive call on the rght sub-list
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list) - 1)



my_list = [4, 6, 1, 7, 3, 2, 5]
print(quick_sort(my_list))









# LC QUESTIONS


"""
1. Write a bubble_sort() method in the LinkedList class that will sort the elements of a linked list 
in ascending order using the bubble sort algorithm. The method should update the head and tail pointers 
of the linked list to reflect the new order of the nodes in the list. You can assume that the input 
linked list will contain only integers. You should not use any additional data structures 
to sort the linked list.

Input:
    The LinkedList object containing a linked list with unsorted elements (self).

Output:
    None. The method sorts the linked list in place.

Method Description:
    * If the length of the linked list is less than 2, the method returns and the list is assumed to be 
    already sorted.
    * The bubble sort algorithm works by repeatedly iterating through the unsorted part of the list, 
    comparing adjacent elements and 
    swapping them if they are in the wrong order.
    * The method starts with the entire linked list being the unsorted part of the list.
    * For each pass through the unsorted part of the list, the method iterates through each pair of 
    adjacent elements and swaps them if they are in the wrong order.
    * After each pass, the largest element in the unsorted part of the list will "bubble up" to the 
    end of the list.
    * The method continues iterating through the unsorted part of the list until no swaps are made 
    during a pass.
    * After the linked list is fully sorted, the head and tail pointers of the linked list are updated 
    to reflect the new order of the nodes in the list.

Constraints:
    The linked list can contain duplicates.
    The method should be implemented in the LinkedList class.
    The method should not use any additional data structures to sort the linked list.
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

    def bubble_sort(self):
        if self.length < 2:
            return
        for i in range(self.length - 1):
            current_node = self.head
            for _ in range(self.length - i -1):
                if current_node.next.value < current_node.value:
                    temp = current_node.value
                    current_node.value = current_node.next.value
                    current_node.next.value = temp
                current_node = current_node.next
    
    def bubble_sort_alternate(self):
        # Check if the list has less than 2 elements
        if self.length < 2:
            return
        
        # Initialize the sorted_until pointer to None
        sorted_until = None
        
        # Continue sorting until sorted_until reaches the second node
        while sorted_until != self.head.next:
            # Initialize current pointer to head of the list
            current = self.head
            
            # Iterate through unsorted portion of the list until sorted_until
            while current.next != sorted_until:
                next_node = current.next
                
                # Swap current and next_node values if current is greater
                if current.value > next_node.value:
                    current.value, next_node.value = next_node.value, current.value
                
                # Move current pointer to next node
                current = current.next
            
            # Update sorted_until pointer to the last node processed so that next iteration
            # will not process any node after sorted_until
            sorted_until = current


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
2. Write a selection_sort() method in the LinkedList class that will sort the elements of a linked list 
in ascending order using the selection sort algorithm. The method should update the head and tail 
pointers of the linked list to reflect the new order of the nodes in the list. You can assume that the 
input linked list will contain only integers. You should not use any additional data structures to sort 
the linked list.

Input:
    The LinkedList object containing a linked list with unsorted elements (self).

Output:
    None. The method sorts the linked list in place.

Method Description:
* If the length of the linked list is less than 2, the method returns and the list is assumed to be 
already sorted.
* The selection sort algorithm works by repeatedly finding the smallest element in the unsorted part of 
the list and swapping it with the first element in the unsorted part of the list.
* The method starts with the entire linked list being the unsorted part of the list.
* For each pass through the unsorted part of the list, the method iterates through each element to find 
the smallest element in the unsorted part of the list. Once the smallest element is found, it is swapped 
with the first element in the unsorted part of the list.
* After each pass, the smallest element in the unsorted part of the list will be at the beginning of 
the unsorted part of the list.
* The method continues iterating through the unsorted part of the list until the entire list is sorted.
* After the linked list is fully sorted, the head and tail pointers of the linked list are updated to 
reflect the new order of the nodes in the list.

Constraints:
    The linked list can contain duplicates.
    The method should be implemented in the LinkedList class.
    The method should not use any additional data structures to sort the linked list.
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

    def selection_sort(self):
        if self.length < 2:
            return
        update_node = self.head
        min_node = self.head
        for i in range(self.length - 1):
            current_node = update_node
            for _ in range(self.length - i - 1):
                current_node = current_node.next
                if current_node.value < min_node.value:
                    min_node = current_node
                
            if min_node.value < update_node.value:
                temp = min_node.value
                min_node.value = update_node.value
                update_node.value = temp
            update_node = update_node.next
    
    def selection_sort_alternate(self):
        if self.length < 2:
            return
        current = self.head
        while current.next is not None:
            smallest = current # smallest position for the current iteration of selection sort
            inner_current = current.next
            while inner_current is not None:
                if inner_current.value < smallest.value:
                    smallest = inner_current
                inner_current = inner_current.next
            if smallest != current:
                current.value, smallest.value = smallest.value, current.value        
            current = current.next
        self.tail = current # update tail



"""
3. Write an insertion_sort() method in the LinkedList class that will sort the elements of a linked list 
in ascending order using the insertion sort algorithm.
The method should update the head and tail pointers of the linked list to reflect the new order of the 
nodes in the list.
You can assume that the input linked list will contain only integers. You should not use any additional 
data structures to sort the linked list.

Input:
    The LinkedList object containing a linked list with unsorted elements (self).

Output:
    None. The method sorts the linked list in place.

Method Description:
* If the length of the linked list is less than 2, the method returns and the list is assumed to be 
already sorted.
* The first element of the linked list is treated as the sorted part of the list, and the second element 
is treated as the unsorted part of the list.
* The first element of the sorted part of the list is then disconnected from the rest of the list, 
creating a new linked list with only one element.
* The method then iterates through each remaining node in the unsorted part of the list.
* For each node in the unsorted part of the list, the method determines its correct position in the 
sorted part of the list by comparing its value with the values of the other nodes in the sorted part of 
the list.
* Once the correct position has been found, the node is inserted into the sorted part of the list at the 
appropriate position.
* After all the nodes in the unsorted part of the list have been inserted into the sorted part of the 
list, the head and tail pointers of the linked list are updated to reflect the new order of the nodes 
in the list.

Constraints:
    The linked list can contain duplicates.
    The method should be implemented in the LinkedList class.
    The method should not use any additional data structures to sort the linked list.
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

    
    def insertion_sort(self):
        if self.length < 2:
            return

        sorted_list_head = self.head # sorted_list_head points to the first element of the sorted
        # part of the linked list
        unsorted_list_head = self.head.next
        sorted_list_head.next = None # remove the head (the initially assumed sorted part) from the 
        # linked list chain. Now, the sorted part becomes seperated from the linked list.
        
        while unsorted_list_head is not None: # unsorted_list_head is the first element of the unsorted
            # part of the linked list
            current = unsorted_list_head # current is the next element in the unsorted part at each iteration
            unsorted_list_head = unsorted_list_head.next
            # insert current before the sorted_list_head if value of current < value of sorted_list_head
            # and then set the new sorted_list_head as current
            if current.value < sorted_list_head.value: # sorted_list_head here is the first element of
                # the sorted part
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                # if value of current > value of sorted_list_head, traverse the sorted part of the
                # linked list until you reach the end of the sorted part and find a node whose next node value
                # is greater than the value of current. Then, current is inserted between this node and its
                # next node which has value > current.value
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
        
        self.head = sorted_list_head # update the head of the linked list as the head of the sorted part
        # because, after all iterations, the entire linked list will be in the sorted part.
        temp = self.head
        # start from the head and traverse to the tail of the linked list
        while temp.next is not None:
            temp = temp.next
        self.tail = temp # update the tail of the linked list
            





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
4. The merge method takes in another LinkedList as an input and merges it with the current LinkedList. 
The elements in both lists are assumed to be in ascending order, but the input lists themselves do not 
need to be sorted.

Parameters=
    other_list (LinkedList): the other LinkedList to merge with the current list

Return Value
    This method does not return a value, but it modifies the current LinkedList to contain the merged list.


Example:
    l1 = LinkedList(1)
    l1.append(3)
    l1.append(5)
    l1.append(7)
    
    l2 = LinkedList(2)
    l2.append(4)
    l2.append(6)
    l2.append(8)
    
    l1.merge(l2)
 
# The current list (l1) now contains the merged list [1, 2, 3, 4, 5, 6, 7, 8]
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

    def merge(self, other_list):
        dummy = Node(0) # create a dummy node to grow the merged linked-list
        top = dummy # for keeping track of head
        current_node = self.head
        other_node = other_list.head
        while (current_node is not None and other_node is not None):
            if other_node.value < current_node.value:
                dummy.next = other_node
                other_node = other_node.next
                self.length += 1
            else:
                dummy.next = current_node
                current_node = current_node.next
            dummy = dummy.next
        while (current_node is not None):
            dummy.next = current_node
            current_node = current_node.next
            dummy = dummy.next
        while (other_node is not None):
            dummy.next = other_node
            other_node = other_node.next
            self.length += 1
            dummy = dummy.next
        # set tail and head
        self.tail = dummy
        self.head = top.next

                


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()

