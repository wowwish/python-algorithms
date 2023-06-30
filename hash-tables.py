# Python has an in-built hash table data structure called Dictionary.
# data is stored in a hash table as ket-value pairs. The key is similar to the index of an array, 
# but can also be a string and dictionary keys do not have any order like the array indices.
# A hash table has a hash function or method that performs a hash on a key which gives back an address
# in memory to store the corresponding key and value pair.

# A hash function used in the hash table should be one-way only (the ouput cannot be used to get 
# back the input) and deterministic (the same input should generate the same output consistently).

# In a hash table, a collision happens when a key-value pair is put in a memory address where
# there is already a key-value pair. There are two popular ways of addressing collision:
#   * seperate chaining: put multiple key-value pairs in the same memory location
#   * linear probing: in a collision situation, keep going up or down the colliding memory location
#     until you reach an empty memory location and put the key-value pair in the empty spot.

# Having a prime number of memory addresses for building hash tables increases the randomness in the
# distribution of the key-value pairs in the hash table and minimizes the number of collisions.

# The Big-O for hash table for INSERT and KEY LOOKUP is O(N) in the worst case where all key-value pairs
# are placed into the same memory location due to collision (typically a linked-list will be used
# to put multiple key-value pairs in the same memory address). But in the real world, we can expect
# a time complexity of O(1) for INSERT and KEY LOOKUP for a hash table due to random distribution of the
# key-value pairs across the memory space allocated for the hash table. 

# Searching for a value is faster in a binary search tree which has a time complexity of O(logN) 
# compared to a hash table which has a Big-O of O(N) for VALUE LOOKUP.

class HashTable:
    def __init__(self, size=7):
        # Assign a list that can hold 'size' number of items as the memory address space for the 
        # hash table. All these memory locations will initially hold None values.
        self.data_map = [None] * size

    # The hash function for the hash table
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) # ord() gives ASCII number of a character
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i, " : ", val)
    

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())




# LC QUESTIONS


"""
1. Write a function item_in_common(list1, list2) that takes two lists as input and returns True if 
there is at least one common item between the two lists, False otherwise.

Use a dictionary to solve the problem that creates an O(n) time complexity.
"""

def item_in_common(list1, list2):
    my_dict = {}
    for item in list1:
        my_dict[item] = True
    for item in list2:
        if item in my_dict: # O(1) time complexity for lookup in dictionary using 'in' operator (average case)
            return True
    return False


"""
2. Problem: Given an array of integers nums, find all the duplicates in the array using a hash table 
(dictionary).

Input:
    A list of integers nums.
Output:
    A list of integers representing the numbers in the input array nums that appear more than once. 
    If no duplicates are found in the input array, return an empty list [].
"""

def find_duplicates(nums):
    visited_nums = {}
    duplicates = []
    for i in range(len(nums)):
        if nums[i] in visited_nums:
            visited_nums[nums[i]] += 1
        else:
            visited_nums[nums[i]] = 1
    for key in visited_nums.keys():
        if visited_nums[key] > 1:
            duplicates.append(key)
    return duplicates


"""
3. You have been given a string of lowercase letters.
Write a function called first_non_repeating_char(string) that finds the first non-repeating character 
in the given string using a hash table (dictionary). If there is no non-repeating character in the 
string, the function should return None.
For example, if the input string is "leetcode", the function should return "l" because "l" is the first 
character that appears only once in the string. Similarly, if the input string is "hello", the function 
should return "h" because "h" is the first non-repeating character in the string.
"""

def first_non_repeating_char(string):
    char_freq = {}
    for i in range(len(string)):
        char_freq[string[i]] = char_freq.get(string[i], 0) + 1
    for key in char_freq.keys():
        if char_freq[key] == 1:
            return key
    return None


"""
4. You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.
For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should 
return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each 
other, the next two strings are anagrams of each other, and the last string has no anagrams in the input 
array.
You need to implement the group_anagrams(strings) function and return a list of lists, where each inner 
list contains a group of anagrams according to the above requirements.
"""

def group_anagrams(strings):
    anagrams = {}
    for i in range(len(strings)):
        canonical_string = ''.join(sorted(strings[i]))
        if canonical_string in anagrams:
            anagrams[canonical_string].append(strings[i])
        else:
            anagrams[canonical_string] = [strings[i]]
    return list(anagrams.values())


"""
5. Given an array of integers nums and a target integer target, find the indices of two numbers in the 
array that add up to the target.
The main challenge here is to implement this function in one pass through the array. This means you 
should not iterate over the array more than once. Therefore, your solution should have a time complexity 
of O(n), where n is the number of elements in nums.

Input:
    A list of integers nums.
    A target integer target.
Output:
    A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].
"""

def two_sum(nums, target):
    visited_nums = {}
    for i in range(len(nums)):
        if (target - nums[i]) in visited_nums:
            return [visited_nums[target-nums[i]], i]
        else:
            visited_nums[nums[i]] = i
    return []


"""
6. Given an array of integers nums and a target integer target, write a Python function called 
subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum 
using a hash table (dictionary).

Your function should take two arguments:
    nums: a list of integers representing the input array
    target: an integer representing the target sum

Your function should return a list of two integers representing the starting and ending indices of 
the subarray that adds up to the target sum. If there is no such subarray, your function should 
return an empty list.
Note that there may be multiple subarrays that add up to the target sum, but your function only needs 
to return the indices of any one such subarray. Also, the input list may contain both positive and 
negative integers.
"""

def subarray_sum(nums, target):
    sum_index = {0: -1} # A hash table to store the running sum and last visited index from start
    current_sum = 0 # cumulative sum of the elements of 'nums' till the currently visited index
    for i in range(len(nums)):
        current_sum += nums[i]
        # if (current_sum - target) is positive, ie, current_sum > target, and there is a sum
        # equivalent to this difference in the hash table, we return the starting index to
        # the index (value) using the hash table (use the difference as key to get index right
        # after the difference in the hash table).
        # For example: given nums = [1, 2, 3, 4, 5] and target = 9, when i = 3, current_sum
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i # if current_sum < target, add the current_sum and currently
        # processed index to the hash table
    return [] # If the current_sum is never >= target, return empty list






# Sets are similar to dictionaries except that instead of having key/value pairs they only have 
# the keys but not the values.
# Like dictionaries, they are implemented using a hash table.
# Sets can only contain unique elements (meaning that duplicates are not allowed). 
# They are useful for various operations such as finding the distinct elements in 
# a collection and performing set operations such as union and intersection.
# They are defined by either using curly braces {} or the built-in set() function like this:

# Create a set using {}
my_set = {1, 2, 3, 4, 5}
 
# Create a set using set()
my_set = set([1, 2, 3, 4, 5])


# Once a set is defined, you can perform various operations on it, such as adding or removing elements, 
# finding the union, intersection, or difference of two sets, and checking if a given element is a 
# member of a set.
# Here are some examples of common set operations in Python:

# Add an element to a set
# If the number 6 is already in the set it will not be added again.
my_set.add(6)
 
# Update is used to add multiple elements to the set at once. 
# It takes an iterable object (e.g., list, tuple, set) as an 
# argument and adds all its elements to the set. 
# If any of the elements already exist in the set, 
# they are not added again.
my_set.update([3, 4, 5, 6])
 
# Removing an element from a set
my_set.remove(3)
 
# Union of two sets
other_set = {3, 4, 5, 6}
union_set = my_set.union(other_set)
 
# Intersection of two sets
intersection_set = my_set.intersection(other_set)
 
# Difference between two sets
difference_set = my_set.difference(other_set)
 
# Checking if an element is in a set
if "hello" in my_set:
    print("Found hello in my_set")



"""
7. You have been given a list my_list with some duplicate values. Your task is to write a Python 
program that removes all the duplicates from the list using a set and then prints the updated list.
You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a 
parameter and returns a new list with no duplicates.
Your function should not modify the original list, instead, it should create a new list with unique 
values and return it.
"""


def remove_duplicates(my_list):
    new_list = list(set(my_list))
    return new_list


"""
8. Write a function called has_unique_chars that takes a string as input and returns True if all the 
characters in the string are unique, and False otherwise.
For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should 
return False.
"""


def has_unique_chars(instring):
    uniq_char = set(instring)
    if len(uniq_char) == len(instring):
        return True
    return False


"""
9. You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task 
is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns 
a list of all such pairs.
"""


def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    result = []
    for n in arr2:
        if (target - n) in set1:
            result.append((target - n, n))
    return result


"""
10. Given an unsorted array of integers, write a function that finds the length of the 
longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than 
the previous element).
Use sets to optimize the runtime of your solution.
    Input: An unsorted array of integers, nums.
    Output: An integer representing the length of the longest consecutive sequence in nums.
"""


def longest_consecutive_sequence(nums):
    uniq_nums = set(nums)
    longest = 0
    for i in range(len(nums)):
        subseq_len = 0
        n = nums[i]
        while (n in uniq_nums):
            subseq_len += 1
            n += 1
        longest = max(longest, subseq_len)
    return longest




