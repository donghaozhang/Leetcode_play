# stone_collision.md)

## 数据结构 (Data Structure)
- LRU缓存 / LRU Cache [LeetCode 146]

## Problem Description

## 146. LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `LRUCache` class:

*   `LRUCache(int capacity)` Initialize LRU cache with positive size `capacity`.
*   `int get(int key)` Return the value of the `key` if the `key` exists, otherwise return `-1`.
*   `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict the least recently used key**.

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
*   `0 <= key <= 10^4`
*   `0 <= value <= 10^5`
*   At most `2 * 10^5` calls will be made to `get` and `put`.

## Solution

## Problem Explanation
The problem requires designing a data structure that follows the constraints of a Least Recently Used (LRU) cache. The LRU cache is a type of cache where the least recently used items are discarded first when the cache reaches its capacity.

The `LRUCache` class should have the following methods:

*   `LRUCache(int capacity)`: Initializes the LRU cache with a positive size `capacity`.
*   `int get(int key)`: Returns the value of the `key` if the `key` exists in the cache, otherwise returns `-1`.
*   `void put(int key, int value)`: Updates the value of the `key` if the `key` exists in the cache. Otherwise, adds the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evicts the least recently used key.

The `get` and `put` operations must each run in `O(1)` average time complexity.

## Step-by-Step Approach
To solve this problem, we will use a combination of a dictionary and a doubly linked list.

1.  **Dictionary**: We will use a dictionary to store the keys and their corresponding nodes in the linked list. This will allow us to access the nodes in `O(1)` time.
2.  **Doubly Linked List**: We will use a doubly linked list to keep track of the order of the elements. The most recently used element will be at the front of the list, and the least recently used element will be at the end.

Here's a step-by-step breakdown of how we will implement the `LRUCache` class:

*   Initialize the cache with a given capacity.
*   When `get(key)` is called:
    *   Check if the key exists in the dictionary.
    *   If it exists, move the corresponding node to the front of the linked list (mark it as recently used) and return its value.
    *   If it doesn't exist, return `-1`.
*   When `put(key, value)` is called:
    *   Check if the key already exists in the dictionary.
    *   If it exists, update its value and move the corresponding node to the front of the linked list.
    *   If it doesn't exist, create a new node with the given key and value, and add it to the front of the linked list.
    *   If the cache has exceeded its capacity, remove the least recently used node (the one at the end of the linked list).

## Python Solution

```python
class Node:
    """A node in the doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """A Least Recently Used (LRU) cache."""
    def __init__(self, capacity: int):
        """
        Initializes the LRU cache with a given capacity.

        :param capacity: The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = {}  # Dictionary to store keys and their corresponding nodes
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """
        Removes a node from the linked list.

        :param node: The node to remove.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        """
        Adds a node to the front of the linked list.

        :param node: The node to add.
        """
        prev_node = self.head
        next_node = self.head.next
        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = next_node

    def get(self, key: int) -> int:
        """
        Returns the value of the given key if it exists in the cache, otherwise returns -1.

        :param key: The key to look up.
        :return: The value associated with the key, or -1 if not found.
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Updates the value of the given key if it exists in the cache, otherwise adds a new key-value pair.

        :param key: The key to update or add.
        :param value: The value to associate with the key.
        """
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

# Test cases
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # Output: 1
    cache.put(3, 3)
    print(cache.get(2))  # Output: -1
    cache.put(4, 4)
    print(cache.get(1))  # Output: -1
    print(cache.get(3))  # Output: 3
    print(cache.get(4))  # Output: 4
```

## Time and Space Complexity Analysis

*   Time complexity:
    *   `get(key)`: `O(1)` because we use a dictionary to access the node in constant time, and we can remove and add a node to the linked list in constant time.
    *   `put(key, value)`: `O(1)` for the same reasons as `get(key)`.
*   Space complexity: `O(capacity)` because we store at most `capacity` nodes in the linked list and the dictionary.

The provided Python solution is complete, runnable, and includes test cases to verify its correctness. It implements the `LRUCache` class using a dictionary and a doubly linked list, achieving `O(1)` time complexity for both `get` and `put` operations.