# Stack is a data structure that follows first-in-first-out (FIFO)
# Queue is a data structure that follows last-in-first-out (LIFO)

# In Python, a list can be used as a stack. Such an implementation will only append and pop items
# from the end of the list for efficiency (prevent re-indexing - O(1) time complexity). 

# Another more efficient way to implement a stack is to use a singly-linked list where both
# adding and removing elements is done from the "head" or "top" of the linked-list for efficiency
# (prevent traversal). The "head" and "tail" of the linked-list are renamed as "top" and "bottom" 
# (optional) when it is used as a stack.

# A queue when implemented as a list inefficient (O(N) on one and and O(1) on other end in terms of 
# time complexity). A linked-list based implementation of queue is much more efficient with O(1) time
# complexity for both "enqueue" (or addition) and "dequeue" (or removal) operations. Enqueue can be
# performed at the end of the linked-list and Dequeue can be performed from the start of the list to
# prevent linked-list traversal and achieve O(1) time complexity for both the operations.
# In a linked-list implementation of a queue, the "head" and "tail" are renamed as "first" and "last".

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
my_stack.print_stack()
print('\n') 
print(my_stack.pop().value)


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last == None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    
print('\n\n')
my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.print_queue()
print('\n')
print(my_queue.dequeue().value)
print(my_queue.dequeue().value)
print(my_queue.dequeue())
print(my_queue.dequeue())






# LC QUESTIONS

"""
1. Create a constructor for Class Stack that implements a new stack with an empty list called stack_list.
"""


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()


"""
2. Check to see if a string of parentheses is balanced or not.
By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in 
the correct order. For example, the string "((()))" has three pairs of balanced parentheses, so it is 
a balanced string. On the other hand, the string "(())))" has an imbalance, as the last two parentheses 
do not match, so it is not balanced.  Also, the string ")(" is not balanced because the close 
parenthesis needs to follow the open parenthesis.

Your program should take a string of parentheses as input and return True if it is balanced, or False 
if it is not. In order to solve this problem, use a Stack data structure.
"""


def is_balanced_parentheses(parantheses):
    parantheses_stack = Stack()
    for char in parantheses:
        if char == '(':
            parantheses_stack.push('(')
        if char == ')':
            out = parantheses_stack.pop()
            if out is None:
                return False
    if parantheses_stack.size() > 0:
        return False
    else:
        return True


"""
3. The reverse_string function takes a single parameter string, which is the string you want to reverse.
Return a new string with the letters in reverse order.
"""


def reverse_string(string):
    str_stack = Stack()
    reverse = ''
    for char in string:
        str_stack.push(char)
    while str_stack.size() > 0:
        reverse += str_stack.pop() 
    return reverse


"""
4. The sort_stack function takes a single argument, a Stack object.  The function should sort the 
elements in the stack in ascending order (the lowest value will be at the top of the stack) using 
only one additional stack. 

The function should use the pop, push, peek, and is_empty methods of the Stack object.
Note: This is a new function, not a method within the Stack class.
This will use the Stack class we created in these coding exercises:
The function should perform the following tasks:

    Create a new instance of the Stack class called sorted_stack which will hold elements
    in descending order that are less than current top of the input stack.
    
    While the input stack is not empty, perform the following:
        Pop the top element from the input stack and store it in a variable temp.
    
        While the sorted_stack is not empty and its top element is greater than temp, pop the top element 
        from sorted_stack and push it back onto the input stack.

        Push the temp variable onto the sorted_stack.

        Once the input stack is empty, transfer the elements back from sorted_stack to the input stack. 
        To do this, while sorted_stack is not empty, pop the top element from sorted_stack and push it 
        onto the input stack.
"""


def sort_stack(input_stack):
    sorted_stack = Stack() # auxiliary stack for help
    while not input_stack.is_empty():
        temp = input_stack.pop() # take the top element from input stack
        while not sorted_stack.is_empty() and sorted_stack.peek() > temp: 
            # whenever the auxiliary stack has atleast one element, compare its top element with the
            # top element of input stack and push all current elements from auxiliary stack > temp into
            # the input stack. The use of while loops is important here. With each iteration of the
            # outer loop, the top element of the input stack is checked with the auxiliary stack and 
            # elements greater than it from the auxiliary stack are pushed back into the input stack.
            # Finally the top element that was used for checking is pushed back in to the auxiliary stack.
            
            # REMEMBER TO ALWAYS VISUALIZE A STACK IN A VERTICAL SENSE AND NOT IN A HORIZONTAL SENSE
            # LIKE A LIST!
            
            # This grows the auxiliary stack is such a way that that after all the iterations, the auxiliary
            # stack contains all the input stack elements sorted in descending order. Now transfer all
            # the elements from the sorted stack to the input stack and this makes the input stack sorted
            # in ascending order.
            input_stack.push(sorted_stack.pop())
        sorted_stack.push(temp) # fill the auxiliary stack with temp at top if it is empty or if its current
        # top element is not > temp
        print('--------------')
        sorted_stack.print_stack()
        print('--------------')
    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())

my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

# print("\nStack after sort_stack:")
# my_stack.print_stack()


"""
5. You are given a class MyQueue which implements a queue using two stacks. Your task is to implement 
the enqueue method which should add an element to the back of the queue.

To achieve this, you can use the two stacks stack1 and stack2. Initially, all elements are stored in 
stack1 and stack2 is empty. In order to add an element to the back of the queue, you need to first 
transfer all elements from stack1 to stack2 using a loop that pops each element from stack1 and 
pushes it onto stack2.

Once all elements have been transferred to stack2, push the new element onto stack1. Finally, 
transfer all elements from stack2 back to stack1 in the same way as before, so that the queue 
maintains its ordering.

Your implementation should satisfy the following constraints:
    * The method signature should be def enqueue(self, value).
    * The method should add the element value to the back of the queue.

You have been tasked with implementing a queue data structure using two stacks in Python, and you 
need to write the dequeue method.
The dequeue method should remove and return the first element in the queue.
"""

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if len(self.stack1) == 0:
            return None
        return self.stack1.pop()
            
    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0