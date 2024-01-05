# INDEXED PRIORITRY QUEUE

# An Indexed Priority Queue is a traditional priority queue variant which on top of the
# regular priority queue operations, supports quick updates and deletionsof key-value pairs.
# It allows to quickly lookup and dynamically change values in the priority queue, on the fly.
# A birectional mapping between the N keys of and the domain [0, N) is created for the 
# indexed priority queue using a bidirectional hash table. Keep in mind that priority queues
# are implemented as heaps under the hood, which internally use an arrays and we want to 
# facilitate indexing into this array in the indexed priority queue.
# Often, the keys themselves are integers in the range [0, N), so there is no need for
# the mapping, but it is handy to be able to support any type of key (like names).

# If 'K' is the key we want to update in the indexed priority queue, first we get the
# key's index: ki = map[K], then use 'ki' with the indexed priority queue:
#   * delete(ki) - delete a key
#   * valueOf(ki) - get the value associated with a key
#   * contains(ki) - check if a key exists in the priority queue
#   * peekMinKeyIndex() - get the index of the key with the smallest value
#   * pollMinKeyIndex() - 
#   * peekMinValue() - getting the smallest value in the indexed priority queue
#   * pollMinValue() - 
#   * insert(ki, value) - insert key-value pairs
#   * update(ki, value) - update key-value pairs
#   * decreaseKey(ki, value) - specialized update operations
#   * increaseKey(ki, value) - specialized update operations

# The IPQ can be implemented in several ways using specialized heaps for optimizations.
# Here, we will look at a Binary Heap based implementation where the time complexities
# are either O(1) or O(logN). We will implement a Min IPQ where the key with the lowest
# value is taken out first and assumed to have the highest priority. Each key is assigned
# a unique index value between [0, N). Each key is also assigned its value. To access the
# value for any given key 'k', find its key index (ki) and do a lookup in the 'vals' array
# maintained by the IPQ.

# Recall that a very common way to represent a binary heap is with an array since every
# node is indexed sequentially.

"""
Let 'i' be the current node (zero based).
left child index: 2i + 1 (zero based)
right child index: 2i + 2 (zero based)

TREE REPRESENTATION:

                                  (0)
                                   9
                                  /  \  
                                 /    \
                                /      \
                               /        \
                              /          \
                             /            \ 
                        (!) /              \  (2)
                          8                 7
                        /   \              / \
                      /      \            /   \       
                (3)  6    (4) 5      (5) 1     2 (6)
                    / \       / \       / \
                   /   \     /   \     /   \ 
                  2     2   3     4   0    insertion position to maintain complete tree structure
                (7)    (8)  (9) (10) (11)  (insertion point for all intermediate nodes to have 
                                            two children in the binary tree/heap)

                                            
HEAP REPRESENTATION:

        ---------------------------------------------------------------------
        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12  | 13  |  14 |
        ---------------------------------------------------------------------
        | 9 | 8 | 7 | 6 | 5 | 1 | 2 | 2 | 2 | 3 | 4  |  0 | n/a | n/a | n/a |
        ---------------------------------------------------------------------

Q: What are the children of the node at index 4?
        left child = 2 * 4 + 1 = 9
        right child = 2 * 4 + 2 = 10


Suppose we insert the value '8'. This would violate the heap invatiant (the binary search 
tree invariant where the left child value should be < than parent value and right child value 
should be > parent value). So, we bubble/sift up the value until the heap invariant/binary search 
tree invariant is met:

TREE REPRESENTATION:

                                  (0)
                                   9
                                  /  \  
                                 /    \
                                /      \
                               /        \
                              /          \
                             /            \ 
                        (!) /              \  (2)
                          8                  7
                        /   \              /  \
                      /      \            /    \       
                (3)  6    (4) 5      (5) 1      2 (6)
                    / \       / \       / \    / \
                   /   \     /   \     /   \  /   \
                  2     2   3     4   0    8 
                (7)    (8)  (9) (10) (11) (12)  
                                            

                                            
HEAP REPRESENTATION:

        ---------------------------------------------------------------------
        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12  | 13  |  14 |
        ---------------------------------------------------------------------
        | 9 | 8 | 7 | 6 | 5 | 1 | 2 | 2 | 2 | 3 | 4  |  0 |  8  | n/a | n/a |
        ---------------------------------------------------------------------


In a traditional Priority Queue, to remove items, we search for the element to remove 
and then swap it with the last node (usually the bottom-right most node), perform removal, 
and finally bubble up or down the swapped value at the removal node location (the removal
node is checked for the heap invariant/BST invariant).


INDEXED PRIORITY QUEUE AS A BINARY HEAP:

Supose we have N people with different priorities that we need to serve at. Assume that
the priorities can dynamically change and we always want to serve the person with the 
lowest priority (MinBinaryHeap). To figure out who to serve next, we will use a Min Indexed
Priority Queue to sort by the lowest value first. We will maintain two arrays



---------------                                                            (0) <- index of node in heap
|  Key   | ki |                                                           Henry
---------------                                                         ki=7, v=1 
|  Anna  |  0 |                                                       /           \
---------------                                                      /             \
|  Bella |  1 |                                                     /               \
---------------                                                    /                 \
|  Carly |  2 |                                              (1)  /                   \   (2)
---------------                                                George                Anna
|  Dylan |  3 |                                              ki=6, v=2             ki=0, v=3
---------------                                           /         \              /        \
|  Emily |  4 |                                          /           \            /          \
---------------                                         /             \          /            \
|  Fred  |  5 |                                 (3)    /         (4)   \    (5) /              \ (6)
---------------                                     Isaac           James     Laura           Fred
| George |  6 |                                   ki=8, v=6      ki=9, v=5  ki=11, v=4      ki=5, v=9
---------------                                   /     \           /  \         / \           /  \
| Henry  |  7 |                                  /       \         /    \       /   \         /    \
---------------                                 /         \       /      \     /     \       /      \
| Isaac  | 8  |                         (7)    /     (8)   \  (9)/    (10)\   / (11)  \     /        \
---------------                             Dylan       Emily  Bella   Kelly Carly 
| James  | 9  |                             ki=3        ki=4   ki=1    ki=10 ki=2
---------------                             v=17        v=7    v=15    v=16  v=11
| Kelly  | 10 |
---------------
| Laura  | 11 |
---------------


THE vals ARRAY:

           -------------------------------------------------------------------------------------------
    (ki)   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  11 |  12 |  13 |  14 | 
           -------------------------------------------------------------------------------------------
  vals     |  3  |  15 |  11 | 17  |  7  |  9  |  2  |  1  |  6  |  5  |  16 |  4  |  -1 |  -1 |  -1 |
           -------------------------------------------------------------------------------------------
    
THE pm ARRAY:

           -------------------------------------------------------------------------------------------
    (ki)   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  11 |  12 |  13 |  14 | 
           -------------------------------------------------------------------------------------------
  (heap    |  2  |  9  |  11 |  7  |  8  |  6  |  1  |  0  |  3  |  4  |  10 |  5  |  -1 |  -1 |  -1 |
  index)   -------------------------------------------------------------------------------------------
            
THE im ARRAY:

  (heap    -------------------------------------------------------------------------------------------
  index)   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  11 |  12 |  13 |  14 |
           -------------------------------------------------------------------------------------------
    (ki)   |  7  |  6  |  0  |  8  |  9  |  11 |  5  |  3  |  4  |  1  |  10 |  2  |  -1 |  -1 |  -1 |
           -------------------------------------------------------------------------------------------

Arbitrarily assign each person a unique index value between [0, N) - the 'ki' column. The 
initial values placed inside the IPQ - the 'Values' column will be maintained by the IPQ
dynamically, accounting for insertion, deletion and updation of values. Note that the values 
of the key-value pairs of an IPQ can be any comparable data type, not only integers. 
When we insert (ki, v) pairs into an IPQ, we sort by the value associated with each key.
In the heap above, we are sorting by smallest value, since we are working with a min heap.

A key mapping and inverse lookup mapping is required to access the position of the node for
a particular key in the heap, and to get the key of a node at a particular position in the heap.
This is required because the key index does not actually reflect the position of the node with
the key in the heap!

To access the value for any given key 'k', find its key index (ki) and do a lookup in the 'vals'
array maintained by the IPO
Q: What value does the key 'Bella' have in the IPQ ?
 ki for 'Bella' is 1. So 'Bella' has a value of vals[ki] = vals[1] = 15

Q: How to find the index of the node for a particular key in the IPQ ?
 Maintain a Position Map "pm" to tell the index of the node in the heap for a given key index "ki"

Q: Which node represents the key "Dylan"?
 The key index for "Dylan" is 3. Looking at index 3 in the position map tells that the node for
 key "Dylan" is at position 7 in the heap.

Q: How do we go from knowing the position of a node in the heap, to its key and key index?
 create an inverse map "im" to perform this inverse lookup of node index in heap to the key index
 "ki" and the key.

Q: Which key is present in the node at index 2 in the heap?
 A lookup in the inverse map "im" at index 2 gives a key index 0. From this, we can get the key
 which is "Anna".


Insertion and Deletion of keys in an Indexed Priority Queue is similar to a regular priority queue,
except for the additional requirement of maintaining the position map and inverse lookup map with
to reflect the changes caused by these operations (including the bubble-up/sink-down operations -
when two nodes are swappe in the heap during these operations, "pm" and "im" values are also 
swapped correspondingly. Note that since only the nodes are swapped, the key index and values 
remain untouched)


Polling (remove and return key-value pair with the lowest priority - the root node. First, the
root node is exchanged with the bottom-rightmost nodea and the "pm", "im" values are also
swapped correspondingly, then the bottom-rightmost node, which is now the root, is removed. Finally
the heap invariant is checked for the new root node and sink-down is performed if required) in an IPQ 
still has O(logN) time complexity (the root node is swapped with the bottom-rightmost), but Removing a 
specific key-value pair in an IPQ is improved from O(N) in a traditional priority queue, to O(logN) 
since node position lookups are O(1), but repositioning is still O(logN). For removing a specific key,
we first obtain the key index for the key, and use it to get the heap index of the node with that
key. Next, the node to be removed is exchanged with the bottom-rightmost node while also swapping the
corresponding values in key mapper "km" and inverse lookup mapper "im". Then, the bottom-rightmost node
is removed from the heap (tree). Finally, the heap invariant is restored to the new node at the position
of the removed node.


Similar to removal, updates in a min indexed binary heap also takes O(logN) due to O(1) lookup
time to find the node and O(logN) time to adjust where the key-value pair should appear in the heap

Q: how to update "Carly" to have a new value of 1?
 the key index for "Carly" is 2. set val[2] = 1. Finally, satisfy the heap invariant by moving the
 updated node either up or down the heap.


In many applications of the Indexed Priority Queue (such as the Prim's and Dijkstra's Algorithm),
it is often useful to only update a given key when its new value is either always smaller (or larger).
In the event that a worse value is given, the value in the IPQ should not be updated.
In such situations, it is useful to define a more restrictive form of update operation we call
increaseKey(ki, v) and decreaseKey(ki, v)



PSEUDOCODE FOR IMPLEMENTATION OF AN INDEXED PRIORITY QUEUE/MIN INDEXED BINARY HEAP

# Inserts a value into the min indexed binary
# heap. The key index must not already be in
# the heap and the value must not be null
function insert(ki, value):
  values[ki] = value
  # 'sz' is the current size of the heap
  pm[ki] = sz
  im[sz] = ki
  swim(sz) # bubble-up the newly inserted node 
  # from the bottom-most right position in
  # the binary tree to its corresponding
  # position
  sz = sz + 1

# swims up node i (zero based) until heap
# invariant is satisfied (the parent node
# must have lower value than the child node)
function swim(i):
  for (p = (i - 1) / 2; i > 0 and less(i, p)):
    # get the index (p) of the parent of node
    # at 'i' and compare their values. swap
    # the node picked from 'i' with the previous
    # layer's parent until the node at 'i' is
    # bubbled-up to its appropriate position
    # in the min indexed binary heap
    swap(i, p)
    i = p # new position of node picked up from index 'i'
    p = (i - 1) / 2 # new parent

# swap the node indices in the position map 
# array first and then in the inverse 
# lookup array
function swap(i, j):
  pm[im[j]] = i
  pm[im[i]] = j
  tmp = im[i]
  im[i] = j
  im[j] = tmp

# compare values nodes at two indices in the heap
# and return a boolean which indicates if 
# the first node's values is lesser than the
# second node's value.
function less(i, j):
  return values[im[i]] < values[im[j]]


# Deletes the node with the key index 'ki'
# in the heap. The key 'ki' must exist and
# be present in the heap.
function remove(ki):
  # get the heap index of the node having the key
  i = pm[ki]
  # 'sz' is the current size of the heap
  swap(i, sz)
  # reduce the size of the heap by 1
  sz = sz - 1
  # restore heap invariant for the new swapped node
  # which is now in the position of deleted node
  # the swapped node may have to move either up or down
  # the heap tree to satisfy the heap invariant
  sink(i)
  swim(i)
  # update the values map, position map and inverse lookup map
  values[ki] = null
  pm[ki] = -1
  im[sz] = -1


# Sinks the node at index 'i' by swapping
# itself with the smallest of the left or
# right child node
function sink(i):
  while true:
    # calculate the index of left and right child 
    # of node at 'i' from the heap
    left = 2*i + 1
    right = 2*i + 2
    # assume the left child index to have the smallest value
    smallest = left
    # 'sz' is the current size of the heap
    # update the smallest child index to right if value of right child
    # is less than value of left child
    if right < sz and less(right, left):
      smallest = right
    # break if left child index > total nodes in heap or if
    # smallest child value is more than the value of node at 'i'
    if left >= sz or less(i, smallest): # stopping-condition
      break
    swap(smallest, i)
    i = smallest

# Updates the value of a key in the binary
# heap. The key index must exist and the 
# value must not be null.
function update(ki, value):
  # get the heap index for the node carrying the given key
  i = pm[ki]
  # update value of key to new value
  vals[ki] = value
  # satisfy the heap invariant condition by moving the updated
  # node either up or down the heap tree. We perform both operations
  # here because to cover all possible cases.
  swim(i)
  sink(i)

# For both increaseKey() and decreaseKey(), assume ki and value
# are valid inputs and we are dealing with a min indexed binary
# heap
function decreaseKey(ki, value):
  # only update the value of key to new value
  # when new value < old value
  if less(value, values[ki]):
    values[ki] = value
    swim(pm[ki]) # satisfy heap invariant (new value < old value and
    # needs to be bubbled up)

function increaseKey(ki, value):
  # only update the value of key to new value
  # when old value < new value
  if less(values[ki], value):
    values[ki] = value
    sink(pm[ki]) # satisfy heap invariant (new value > old value and needs 
    # to be sent down the heap)
"""


# SOURCE CODE FOR INDEXED PRIORITY QUEUE USING A D-ARY HEAP


"""
import static java.lang.Math.max;
import static java.lang.Math.min;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

public class minIndexedDHeap <T extends Comparable<T>> {
  
  // Current number of elements in the heap
  private int sz;

  // Maximum number of elements in the heap
  private final int N;

  // The degree of every node in the heap
  private final int D;

  // Lookup arrays to track the child/parent indexes of each node
  private final int[] child, parent;

  // The Position Map (pm) maps Key Indexes (ki) to where the position of that
  // key is represented in the priority queue in the domain [0, sz).
  public final int[] pm;

  // The Inverse Map (im) stores the indexes of the keys in the range
  // [0, sz) which make up the priority queue. It should be noted that
  // 'im' and 'pm' are inverses of each other, so: pm[im[i]] = im[pm[i]] = i
  public final int[] im;

  // The values associated with the keys. It is very important to note
  // that this array is indexed by the key indexes (aka 'ki').
  public final Object[] values;

  // Initializes a D-ary heap with a maximum capacity of maxSize
  public MinIndexedDHeap(int degree, int maxSize) {
    if (maxSize <= 0) throw new IllegalArgumentException("maxSize <= 0");
    
    D = max(2, degree);
    // The minimal heap will have atleast D+1 nodes
    N = max(D+1, maxSize);

    im = new int[N];
    pm = new int[N];
    child = new int[N];
    parent = new int[N];
    values = Object[N];

    // D-ary heap will have D children for each parent
    for (int i = 0; i < N; i++) {
      // for a Binary Heap, 'D' will be 2
      parent[i] = (i-1) / D; 
      child[i] = i*D + 1;
      // assign -1 for all values of 'pm' and 'im' initially
      pm[i] = im[i] = -1;
    }
  }

  public int size() {
    return sz;
  }

  public boolean isEmpty() {
    return sz == 0; // does heap have no nodes
  }

  public boolean contains(ki) {
    // check validity of 'ki'
    keyInBoundsOrThrow(ki);
    // if key at 'ki' is not present in the heap, 'pm[ki]' will return -1
    return pm[ki] != -1;
  }

  public int peekMinKeyIndex() {
    isNotEmptyOrThrow(); // throw error if heap is empty
    return im[0]; // return the key index of root node of the min heap
  }

  public int pollMinKeyIndex() {
    // copy the root node of the min heap, delete it and
    // return the copy
    int minki = peekMinKeyIndex();
    delete(minki);
    return minki;
  }

  @SuppressWarnings("unchecked")
  public T peekMinValue() {
    isNotEmptyOrThrow();
    // return the value for key index of root node of min heap
    return (T) values[im[0]];
  }

  public T pollMinValue() {
    // create a copy of value for key index of root node of min heap
    // then delete the node and then return the value
    T minValue = peekMinValue();
    delete(peekMinKeyIndex());
    return minValue;
  }

  public void insert(int ki, T value) {
    if(contains(ki)) {
      throw new IllegalArgumentException("index already exists; recieved: " + ki);
    }
    valueNotNullOrThrow(value); // handle null value cases
    // insert the new key into the new node at position 'sz' in the heap
    pm[ki] = sz;
    im[sz] = ki;
    // set the value for the new key
    values[ki] = value;
    swim(sz++); // use current value of 'sz' for the swim() call and then increment 'sz'
    // this makes the heap one element larger after insertion
    }
  }

  @SuppressWarnings("unchecked")
  public T valueOf(int ki) {
    keyExistsOrThrow(ki); // handle invalid keys
    return (T) values[ki];
  }

  @SuppressWarnings("unchecked")
  public T delete(int ki) {
    keyExistsOrThrow(ki);
    // get the position of the node in the heap with given key
    final int i = pm[ki];
    // swap the  node with the last position in the heap
    // with the node of the given key
    swap(i, --sz);
    // The new node (bottom-right most) that was swapped in place of the deleted node's
    // original position may have to move either up or down the heap tree to
    // satisfy the heap invariant condition, so we call both sink() and swim() on the new
    // node.
    sink(i);
    swim(i);
    T value = (T) values[ki];
    values[ki] = null;
    pm[ki] = -1;
    im[sz] = -1;
    return value; 
  }

  @SuppressWarnings("unchecked")
  public T update(int ki, T value) {
    keyExistsAndValueNotNullOrThrow(ki, value);
    final int i = pm[ki];
    T oldValue = (T) value[ki]; // explicit type conversion of new value
    values[ki] = value;
    // after setting the key's value to new value, the heap has to be updated
    // by moving the update node to its appropriate position within the heap
    // such that it satisfies the heap invariant. We use both sink() and swim()
    // because the updated node may have to be moved either up or down the heap
    // tree to satisfy the heap invariant.
    sink(i);
    swim(i);
    return oldValue;
  }

  // Strictly decreases the value associated with 'ki' to 'value'
  public void decrease(int ki, T value) {
    keyExistsAndValueNotNullOrThrow(ki, value);
    if(less(value, values[ki])) {
      values[ki] = value;
      swim(pm[ki]);
    }
  }

  // Strictly increases the value associated with 'ki' to 'value'
  public void increase(int ki, T value) {
    keyExistsAndValueNotNullOrThrow(ki, value);
    if (less(values[ki], value)) {
      values[ki] = value;
      sink(pm[ki]);
    }
  }

      /* Helper Functions */
  
  // swap the minChild of a given node at index 'i' with the node itself causing 
  // the node to move down the heap
  private void sink(int i) {
    for (int j = minChild(i); j != -1;) {
      swap(i, j);
      i = j;
      j = minChild(i);
    }
  }

  // swap the node at index 'i' with its parent and continue swapping the node upwards
  // in the heap, until the node's value is no longer smaller than its parent node.
  private void swim(int i) {
    while(less(i, parent[i])) {
      swap(i, parent[i]);
      i = parent[i];
    }
  }

  // From the parent node at index i find the minimum child below it
  private int minChild(int i) {
    // min(sz, from + D) is used because the parent 'from' may have less than 'D' 
    // children if it is the right-most node in the heap
    int index = -1, from = child[i], to = min(sz, from + D);
    for (int i = from; j < to; j++) {
      if less(j, i) {
        index = i = j;
      }
    }
    return index;
  }

  private void swap(int i, int j) {
    // swap the node indexes of the heap in the position map
    pm[im[j]] = i;
    pm[im[i]] = j;
    // swap the key indexes in the inverse lookup map
    int tmp = im[i];
    im[i] = im[j];
    im[j] = tmp;
  }

  // Tests if the value of node i < node j
  @SuppressWarnings("unchecked")
  private boolean less(int i, int j) {
    return ((Comparable<? super T>) values[im[i]]).compareTo(T) values[im[j]] < 0;
  }

  @SuppressWarnings("unchecked")
  private boolean less(Object obj1, Object obj2) {
    return ((Comparable<? super T>) obj1).compareTo((T) obj2) < 0;
  }

  @Override
  public String toString() {
    List<Integer> lst = new ArrayList<>(sz);
    for (int i = 0; i < sz; i++) lst.add(im[i]);
    return lst.toString();
  }

      /* Helper functions to make the code more readable */

  private void iNotEmptyOrThrow() {
    if (isEmpty()) throw new NoSuchElementException("Priority queue underflow");
  }

  private void keyExistsAndValueNotNullOrThrow(int ki, Object value) {
    keyExistsOrThrow(ki);
    valueNotNullOrThrow(value);
  }

  private void keyExistsOrThrow(int ki) {
    if (!contains(ki)) {
      throw new NoSuchElementException("Index does not exist; recieved: " + ki);
    }
  }

  private void valueNotNullOrThrow(Object value) {
    if (value == null) {
      throw new IllegalArgumentException("value cannot be null");
    }
  }

  private void keyInBoundsOrThrow(int ki) {
    if (ki < 0 || ki >= N) {
      throw new IllegalArgumentException("Key index out of bounds; recieved: " + ki);
    }
  }

      /* Test Functions */
  
  // Recursively checks if this heap is a min heap. This method is used
  // for testing purposes to validate the heap invariant.
  public boolean isMinHeap() {
    return isMinHeap(0);
  }

  private boolean isMinHeap(int i) {
    // min(sz, from + D) is used because the node at 'i' may have less than 'D' children
    // in case it is the right-most node in the heap
    int from = child[i], to = min(sz, from + D);
    for (int j = from; j < to; j++) {
      if (!less(i, j)) return false;
      if (!isMinHeap(j)) return false;
    }
    return true;
  }
}

public class MinIndexedBinaryHeap <T extends Comparable<T>> extends MinIndexedDHeap <T> {
  public MinIndexedBinaryHeap(int maxSize) {
    super(2, maxSize);
  }
}
"""