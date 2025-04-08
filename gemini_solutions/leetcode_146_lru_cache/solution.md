# stone_collision.md)

## 数据结构 (Data Structure)
- LRU缓存 / LRU Cache [LeetCode 146]

## Problem Description

```markdown
# 146. LRU Cache

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

*   `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
*   `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
*   `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key`-`value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

**Example 1:**

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

**Constraints:**

*   `1 <= capacity <= 3000`
*   `0 <= key <= 10000`
*   `0 <= value <= 10^5`
*   At most `2 * 10^5` calls will be made to `get` and `put`.
```

## Solution

Okay, let's break down the LRU Cache problem.

## 1. Explanation of the Problem

The goal is to create a data structure, `LRUCache`, that acts like a cache with a fixed `capacity`. A cache stores key-value pairs. The key features are:

1.  **Fixed Size:** The cache can only hold a specific number of items (`capacity`).
2.  **`get(key)` Operation:** Retrieves the value associated with a `key`. If the key exists, it returns the value and marks this key as the *most recently used*. If the key doesn't exist, it returns `-1`.
3.  **`put(key, value)` Operation:** Inserts or updates a key-value pair.
    *   If the `key` already exists, its `value` is updated, and the key is marked as the *most recently used*.
    *   If the `key` doesn't exist, the new pair is added.
        *   If the cache is already full (size equals `capacity`), the *least recently used* (LRU) item must be removed before adding the new item.
        *   The newly added/updated item becomes the *most recently used*.
4.  **Efficiency:** Both `get` and `put` operations must have an average time complexity of O(1).

The "Least Recently Used" policy means that when the cache needs to make space, it discards the item that hasn't been accessed (either by `get` or `put`) for the longest time.

## 2. Step-by-Step Approach

To achieve O(1) time complexity for both `get` and `put`, we need data structures that support fast lookups, insertions, deletions, and maintaining order.

1.  **Fast Lookups (O(1)):** A hash map (dictionary in Python) is ideal for checking if a key exists and retrieving its associated information in O(1) average time. Let's call this `cache`.
2.  **Maintaining Recency Order & Fast Removal/Addition (O(1)):** We need a way to track the usage order (from most recent to least recent) and quickly:
    *   Add an item as the most recent.
    *   Remove the least recent item.
    *   Move an existing item to the most recent position when accessed.
    A **doubly linked list (DLL)** is perfect for this. We can add to the head (most recent) in O(1), remove from the tail (least recent) in O(1), and move any node to the head in O(1) *if we have a pointer to that node*.
3.  **Combining the Structures:**
    *   The hash map (`cache`) will store the `key` as its key and a *pointer/reference to the node in the doubly linked list* as its value. `cache: {key -> DLLNode}`.
    *   The doubly linked list will store the actual `(key, value)` pairs within its nodes. The order in the list will represent the recency, with the head being the most recently used and the tail being the least recently used.

**Detailed Steps:**

1.  **Initialization (`__init__`)**:
    *   Store the `capacity`.
    *   Initialize an empty hash map `self.cache = {}`.
    *   Initialize a doubly linked list. Using dummy `head` and `tail` nodes simplifies edge cases (empty list, removing first/last element).
        *   `self.head = Node(0, 0)` # Dummy head
        *   `self.tail = Node(0, 0)` # Dummy tail
        *   Link them: `self.head.next = self.tail`, `self.tail.prev = self.head`.

2.  **Doubly Linked List Node Structure**:
    *   Define a `Node` class with attributes: `key`, `value`, `prev` (pointer to previous node), `next` (pointer to next node).

3.  **DLL Helper Functions**:
    *   `_remove(node)`: Removes a given `node` from the DLL. Updates `prev` and `next` pointers of adjacent nodes. O(1).
    *   `_add(node)`: Adds a given `node` right after the `head` (making it the most recent). Updates pointers. O(1).

4.  **`get(key)` Implementation**:
    *   Check if `key` is in `self.cache`.
    *   If not, return `-1`.
    *   If yes:
        *   Get the `node` from `self.cache[key]`.
        *   Move this `node` to the front of the DLL (mark as most recently used):
            *   Call `_remove(node)`.
            *   Call `_add(node)`.
        *   Return `node.value`.

5.  **`put(key, value)` Implementation**:
    *   Check if `key` is in `self.cache`.
    *   If yes (key exists):
        *   Get the `node` from `self.cache[key]`.
        *   Update the `node.value = value`.
        *   Move this `node` to the front of the DLL:
            *   Call `_remove(node)`.
            *   Call `_add(node)`.
    *   If no (new key):
        *   Check if the cache is full: `len(self.cache) == self.capacity`.
        *   If full:
            *   Get the least recently used node (the one just before `self.tail`): `lru_node = self.tail.prev`.
            *   Remove it from the hash map: `del self.cache[lru_node.key]`.
            *   Remove it from the DLL: `_remove(lru_node)`.
        *   Create a new `node = Node(key, value)`.
        *   Add the new node to the hash map: `self.cache[key] = node`.
        *   Add the new node to the front of the DLL: `_add(node)`.

## 3. Python Solution

```python
import collections

# Define the structure for the nodes in the Doubly Linked List
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        """
        Initializes the LRU cache with a given capacity.
        Sets up the cache dictionary and the dummy head/tail nodes for the DLL.
        """
        self.capacity = capacity
        self.cache = {}  # Stores key -> Node mapping
        # Initialize Doubly Linked List with dummy nodes
        self.head = Node(0, 0) # Dummy head
        self.tail = Node(0, 0) # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """
        Removes a node from the Doubly Linked List.
        Connects the previous and next nodes directly.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node):
        """
        Adds a node right after the dummy head (making it the most recently used).
        Updates pointers accordingly.
        """
        # New node's pointers
        node.prev = self.head
        node.next = self.head.next
        # Update pointers of surrounding nodes
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """
        Retrieves the value for a key if it exists in the cache.
        If found, moves the corresponding node to the front of the DLL (most recent).
        Returns -1 if the key is not found.
        """
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the front (most recently used)
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Adds or updates a key-value pair in the cache.
        If the key exists, updates its value and moves it to the front.
        If the key is new:
          - If capacity is reached, removes the least recently used item.
          - Adds the new key-value pair to the cache and DLL front.
        """
        # If key already exists, update value and move to front
        if key in self.cache:
            node = self.cache[key]
            # Remove old node position
            self._remove(node)
            # Update value
            node.val = value
            # Add updated node to front
            self._add(node)
            # No need to update self.cache[key] as the node object is the same
        else:
            # If cache is full, remove the least recently used item
            if len(self.cache) >= self.capacity:
                # LRU item is the node just before the dummy tail
                lru_node = self.tail.prev
                # Remove LRU from DLL
                self._remove(lru_node)
                # Remove LRU from cache map
                del self.cache[lru_node.key]

            # Add the new key-value pair
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node) # Add to the front of DLL

# --- Test Cases ---

def run_test_case(operations, values):
    """Helper function to run a sequence of operations and check outputs."""
    obj = None
    results = []
    print(f"--- Running Test ---")
    print(f"Operations: {operations}")
    print(f"Values: {values}")

    for i, op in enumerate(operations):
        val = values[i]
        if op == "LRUCache":
            obj = LRUCache(val[0])
            results.append(None)
            print(f"Instantiated LRUCache({val[0]})")
        elif op == "put":
            obj.put(val[0], val[1])
            results.append(None)
            print(f"put({val[0]}, {val[1]}) -> Cache size: {len(obj.cache)}")
        elif op == "get":
            res = obj.get(val[0])
            results.append(res)
            print(f"get({val[0]}) -> returned: {res}")
        # Optional: Print cache state for debugging
        # if obj:
        #    current_cache = {}
        #    curr = obj.head.next
        #    while curr != obj.tail:
        #        current_cache[curr.key] = curr.val
        #        curr = curr.next
        #    print(f"  Current Cache Order (MRU->LRU): {list(current_cache.items())}")
        #    print(f"  Hash Map: { {k: v.val for k, v in obj.cache.items()} }")


    print(f"Output: {results}")
    print("-" * 20)
    return results

# Example 1 from LeetCode
ops1 = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
vals1 = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
expected1 = [None, None, None, 1, None, -1, None, -1, 3, 4]
output1 = run_test_case(ops1, vals1)
assert output1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {output1}"
print("Test Case 1 Passed!")

# Test Case 2: Capacity 1
ops2 = ["LRUCache", "put", "get", "put", "get", "get"]
vals2 = [[1], [2, 1], [2], [3, 2], [2], [3]]
expected2 = [None, None, 1, None, -1, 2]
output2 = run_test_case(ops2, vals2)
assert output2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {output2}"
print("Test Case 2 Passed!")

# Test Case 3: Update existing key
ops3 = ["LRUCache", "put", "put", "put", "get", "put", "get"]
vals3 = [[2], [1, 1], [2, 2], [1, 10], [1], [3, 3], [2]] # Update 1, then put 3 (evicts 2)
expected3 = [None, None, None, None, 10, None, -1]
output3 = run_test_case(ops3, vals3)
assert output3 == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {output3}"
print("Test Case 3 Passed!")

# Test Case 4: Get causes eviction later
ops4 = ["LRUCache", "put", "put", "put", "get", "get", "put", "get"] # Get 2 makes 1 LRU
vals4 = [[3], [1, 1], [2, 2], [3, 3], [2], [1], [4, 4], [3]] # Put 4 evicts 3
expected4 = [None, None, None, None, 2, 1, None, -1]
output4 = run_test_case(ops4, vals4)
assert output4 == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {output4}"
print("Test Case 4 Passed!")

# Test Case 5: Empty gets
ops5 = ["LRUCache", "get", "get"]
vals5 = [[1], [1], [2]]
expected5 = [None, -1, -1]
output5 = run_test_case(ops5, vals5)
assert output5 == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {output5}"
print("Test Case 5 Passed!")


## Complexity Analysis:

*   **Time Complexity:**
    *   `__init__`: O(1) - Initializing the dictionary and dummy nodes takes constant time.
    *   `get(key)`: O(1) average - Dictionary lookup (`key in self.cache`) is O(1) on average. Removing and adding nodes to the DLL (`_remove`, `_add`) take O(1) time as we have direct references.
    *   `put(key, value)`: O(1) average - Dictionary lookup/insertion/deletion (`key in self.cache`, `self.cache[key] = ...`, `del self.cache[...]`) are O(1) on average. Removing and adding nodes to the DLL (`_remove`, `_add`) take O(1) time.
*   **Space Complexity:** O(capacity) - The hash map (`self.cache`) stores at most `capacity` key-node mappings. The doubly linked list stores at most `capacity` nodes (plus the two dummy nodes). Each node stores a key, value, and two pointers, resulting in constant space per node. Therefore, the total space used is proportional to the `capacity`.

## 4. Test Cases

Included above within the Python solution code block. The test cases cover:

1.  **LeetCode Example 1:** The standard example demonstrating basic puts, gets, and eviction.
2.  **Capacity 1:** Edge case where the cache can only hold one item.
3.  **Update Existing Key:** Ensures updating a key's value also makes it the most recently used.
4.  **Get Operation Affecting LRU:** Demonstrates how a `get` operation changes the recency order and influences subsequent evictions.
5.  **Empty Gets:** Checks behavior when getting keys from an empty or non-containing cache.