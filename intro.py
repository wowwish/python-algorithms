# Different Big(O) (Worst Case) time complexities

# O(N) time complexity examples

def print_items(n):
    for i in range(n):
        print(i)

# print_items(10)

# O(N + N) or O(2N) can be simplified to O(N) by dropping the constant
def print_items2(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


# However, when the two inputs are different, we add the total operations and cannot simplify!
# O(a + b) time complexity is an example for this
def print_two_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)


# Example of O(N^2) time complexity
def print_items3(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# print_items3(10)
    
# O(N^2 + N) can be simplified to O(N^2) by dropping non-dominant terms - N^2 >>> N for large N
def print_items4(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for i in range(n):
        print(n)



# Example of O(1) time complexity

def print_items5(n):
    return n + n + n # constant 3 operations irrespective of value of N


# Example of O(logN) time complexity: Binary Search
def binary_search(n, arr):
    start = 0
    end = len(arr) - 1
    mid = None
    iteration_count = 0
    while(start <= end):
        iteration_count += 1
        print(f'Iteration Number: {iteration_count}')
        mid = int((start + end) / 2)
        if arr[mid] < n:
            start = mid + 1
        elif arr[mid] > n:
            end = mid - 1
        elif arr[mid] == n:
            return mid


print(binary_search(8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        

# LISTS

# <list>.append() and <list>.pop() insert and remove at the end of the list. There is not re-indexing of 
# previous elements upstream of the last index and hence, these two operations have O(1) time complexity.
# However, <list>.pop(0) removes the first element of the list and all the downstream elements have to
# be re-indexed. Same goes for <list>.insert(0, <value>). Hence, insertion and removal from the start
# of the list has time complexity of O(N) because of re-indexing of all the downstream elements.

# To access an element using index, we have O(1) time complexity in a list.



# CLASSES

class Cookie:
    # constructor
    def __init__(self, color):
        self.color = color # This is an attribute that is provided during object creation and will be
        # specific to each instance of this class.
    # instance methods
    def get_color(self): # method to return current color of an instance
        return self.color
    def set_color(self, color): # method to modify color of an instance
        self.color = color


# Objects or instances of the 'Cookie' class
cookie_one = Cookie('green') # cookie_one.color = 'green'
cookie_two = Cookie('blue') # cookie_two.color = 'blue'
print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color(), '\n\n')



# POINTERS

# Pointers in Python work differently with different data types

num1 = 11 # 'num1' is a pointer to the value '11' that is created and stored in memory
num2 = num1 # now, 'num2' is also a pointer to value '11' and it is seperate from 'num1'

print('Before num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)
print('\nnum1 points to:', id(num1)) # id(<var>) gives the memory address where the variable is stored
print('num2 points to:', id(num2))

num2 = 22

print('\nAfter num2 values is updated:')
print('num1 =', num1)
print('num2 =', num2)
print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2), '\n\n')

# INTEGERS ARE STORED AS IMMUTABLE LITERALS IN MEMORY IN PYTHON.


# However, Dictionaries behave differently!

dict1 = {
    'value': 11
}

dict2 = dict1

print('Before value is updated in dictionary:')
print('dict1 =', dict1)
print('dict2 =', dict2)
print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))

dict2['value'] = 22

print('\nAfter value is updated in dictionary:')
print('dict1 =', dict1)
print('dict2 =', dict2)
print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2), '\n\n')

# NOTICE HOW dict1 and dict2 BOTH HAD THEIR VALUES CHANGED AND BOTH POINT TO THE SAME MEMORY ADDRESS
# UNLIKE THE CASE WITH INTEGERS! THIS IS BECAUSE DICTIONARIES ARE MUTABLE DATATYPES IN PYTHON!

# NOW IF WE CREATE ANOTHER DICTIONARY VARIABLE dict3 WITH A NEW VALUE, AND MAKE dict2 POINT TO
# dict3:

dict3 = {
    'value': 33
}

print('Before dict2 is updated:')
print('dict1 =', dict1)
print('dict2 =', dict2)
print('dict3 =', dict3)
print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))
print('dict3 points to:', id(dict3))

dict2 = dict3

print('\nAfter dict2 is updated:')
print('dict1 =', dict1)
print('dict2 =', dict2)
print('dict3 =', dict3)
print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))
print('dict3 points to:', id(dict3))

dict1 = dict2

print('\nAfter dict1 is updated:')
print('dict1 =', dict1)
print('dict2 =', dict2)
print('dict3 =', dict3)
print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))
print('dict3 points to:', id(dict3))

# NOW THE UN-REFERENCED DICTIONARY {'value': 22} TO WHICH dict1 WAS POINTING TO WILL BE REMOVED 
# THROUGH THE PROCESS OF GARBAGE-COLLECTION TO SAVE MEMORY, SINCE THIS DICTIONARY IS NOT POINTED TO
# BE ANY VARIABLE!