"""
1. Given a list of integers nums and an integer val, write a function remove_element that removes 
all occurrences of val in the list in-place and returns the new length of the modified list.
The function should not allocate extra space for another list; instead, it should modify the input 
list in-place with O(1) extra memory.

Input:
    A list of integers nums .
    An integer val representing the value to be removed from the list.

Output:
    An integer representing the new length of the modified list after removing all occurrences of val.

Constraints:
    Do not use any built-in list methods, except for pop() to remove elements.

    It is okay to have extra space at the end of the modified list after removing elements.
"""

def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


"""
2. Write a Python function that takes a list of integers as input and returns a tuple containing the 
maximum and minimum values in the list.

The function should have the following signature:
    def find_max_min(myList):
    
Where myList is the list of integers to search for the maximum and minimum values.
The function should traverse the list and keep track of the current maximum and minimum values. It 
should then return these values as a tuple, with the maximum value as the first element and the minimum 
value as the second element.
For example, if the input list is [5, 3, 8, 1, 6, 9], the function should return (9, 1) since 9 is the 
maximum value and 1 is the minimum value.
"""


def find_max_min(myList):
    min = myList[0]
    max = myList[0]
    for i in range(len(myList)):
        if myList[i] > max:
            max = myList[i]
        if myList[i] < min:
            min = myList[i]
    return (max, min)


"""
3. Write a Python function called find_longest_string that takes a list of strings as an input and 
returns the longest string in the list. The function should iterate through each string in the list, 
check its length, and keep track of the longest string seen so far. Once it has looped through all the 
strings, the function should return the longest string found.
"""


def find_longest_string(strings):
    longest = strings[0]
    for i in range(len(strings)):
        if len(strings[i]) > len(longest):
            longest = strings[i]
    return longest


"""
4. Given a sorted list of integers, rearrange the list in-place such that all unique elements appear at 
the beginning of the list, followed by the duplicate elements. Your function should return the new 
length of the list containing only unique elements. Note that you should not create a new list or use 
any additional data structures to solve this problem. The original list should be modified in-place.

Constraints:
    The input list is sorted in non-decreasing order.

    The input list may contain duplicates.

    The function should have a time complexity of O(n), where n is the length of the input list.

    The function should have a space complexity of O(1), i.e., it should not use any additional 
    data structures or create new lists.


Example:
    Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] Function call: new_length = remove_duplicates(nums) 
    
    Output: new_length = 5 Modified list: nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] (first 5 elements are unique)
    
    Explanation: The function modifies the original list nums in-place, moving unique elements to the 
    beginning of the list, followed by duplicate elements. The new length returned by the function is 5, 
    indicating that there are 5 unique elements in the list. The first 5 elements of the modified list 
    nums are the unique elements [0, 1, 2, 3, 4].
"""


def remove_duplicates(nums):
    if not nums:
        return 0
    write_pointer = 1
    # compare every element with its previous element, if found to be a non-duplicate, then set the
    # element at the write_pointer as this non-duplicate element.
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
    return write_pointer

# ALTERNATIVE SOLUTION
def remove_duplicates_alt(my_list):
    idx = 0
    processed = 0
    while (processed < len(my_list)):
        processed += 1
        j = idx + 1
        while ((my_list[j] == my_list[idx]) and (processed < len(my_list))):
            dup = my_list.pop(j)
            my_list.append(dup)
            processed += 1
        idx += 1
        print(idx)
    return idx 
    
nums = [0, 2, 3, 3]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])

"""
5. You are given a list of integers representing stock prices for a certain company over a period of 
time, where each element in the list corresponds to the stock price for a specific day.
You are allowed to buy one share of the stock on one day and sell it on a later day.
Your task is to write a function called max_profit that takes the list of stock prices as input and 
returns the maximum profit you can make by buying and selling at the right time.
Note that you must buy the stock before selling it, and you are allowed to make only one 
transaction (buy once and sell once).

Constraints:
    Each element of the input list is a positive integer representing the stock price for a specific day.

Function signature: 
    def max_profit(prices):

Example:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Function call: profit = max_profit(prices)
    Output: profit = 5

Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it 
on day 5 (price 6), resulting in a profit of 6 - 1 = 5.
"""


def max_profit(prices):
    buy = prices[0] # minimum buying price for the stock
    profit = 0 # maximum profit possible for the stock given time period and the price everyday
    for i in range(len(prices)):
        # If the current price is lower than minimum price encountered till now, update the minimum
        # buying price.
        if prices[i] < buy:
            buy = prices[i]
        # If the profit obtained by buying at the current minimum buying price and selling at current
        # price is more than the previous highest profit that we obtained, update the maximum possible
        # profit for the stock in the given time period.
        if (prices[i] - buy) > profit:
            profit = prices[i] - buy
    return profit


"""
6. You are given a list of n integers and a non-negative integer k.
Your task is to write a function called rotate that takes the list of integers and an integer k as 
input and rotates the list to the right by k steps.
The function should modify the input list in-place, and you should not return anything.

Constraints:    
    Each element of the input list is an integer.
    The integer k is non-negative.

Function signature: 
    def rotate(nums, k):

Example:
    Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Function call: rotate(nums, k)
    Output: nums = [5, 6, 7, 1, 2, 3, 4]
"""

def rotate(nums, k):
    k = k % len(nums) # to handle edge-case where k > len(nums) slice the list after k elements and 
    # concatenate them in reverse order. The last k elements come first followed by the first (n - k) 
    # elements. nums[:] is used to modify the 'nums' list in-place
    nums[:] = nums[-k:] + nums[:-k]


"""
7. Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous 
subarray (containing at least one number) with the largest sum and returns its sum.
Remember to also account for an array with 0 items.

Function Signature:
    def max_subarray(nums):

Input:
    A list of integers nums.

Output:
    An integer representing the sum of the contiguous subarray with the largest sum.

Example:
    max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    Output: 6
    Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum, which is 6.
"""

# Kadane's algorithm
def max_subarray(nums):
    if len(nums) == 0: # edge-case handling for empty list
        return 0
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

