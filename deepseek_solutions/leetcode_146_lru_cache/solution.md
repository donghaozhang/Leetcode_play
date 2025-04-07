# stone_collision.md)

## 数据结构 (Data Structure)
- LRU缓存 / LRU Cache [LeetCode 146]

## Problem Description

### Problem Description:

Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.

#### Example 1:

**Input:**
```
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
```

**Output:**
```
[null, null, null, 1, null, -1, null, -1, 3, 4]
```

**Explanation:**
```java
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

#### Constraints:

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls will be made to `get` and `put`.

## Solution

### Explanation of the Problem

The LRU (Least Recently Used) cache is a type of cache that evicts the least recently accessed item when the cache reaches its capacity. The goal is to design a data structure that supports two operations:
1. `get(key)`: Retrieve the value associated with the key if it exists in the cache, otherwise return -1. Accessing a key updates its "recently used" status.
2. `put(key, value)`: Add or update the value associated with the key. If the cache is at capacity, evict the least recently used key before adding the new key-value pair.

Both operations must run in O(1) average time complexity.

### Approach
To achieve O(1) time complexity for both `get` and `put`, we can use a combination of a hash map and a doubly linked list:
1. **Hash Map**: Stores keys as keys and nodes (from the doubly linked list) as values for O(1) access.
2. **Doubly Linked List**: Maintains the order of keys based on their usage. The most recently used key is at the front (head), and the least recently used key is at the back (tail).

**Steps:**
1. **Initialization**: Initialize the LRUCache with a given capacity. Set up the hash map and doubly linked list with dummy head and tail nodes to simplify edge cases.
2. **get(key)**:
   - If the key exists in the hash map, move the corresponding node to the front of the list (most recently used) and return its value.
   - If the key does not exist, return -1.
3. **put(key, value)**:
   - If the key exists, update its value and move the node to the front.
   - If the key does not exist:
     - Create a new node and add it to the front.
     - Add the key and node to the hash map.
     - If the cache exceeds capacity, remove the node at the tail (least recently used) and its corresponding entry from the hash map.

### Solution Code
```python
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DLinkedNode()  # dummy head
        self.tail = DLinkedNode()  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self._remove_tail()
                del self.cache[removed.key]
                self.size -= 1

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

# Test cases
def test_lru_cache():
    # Test case 1
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    print("Test case 1 passed")

    # Test case 2: Edge case with capacity 1
    lru = LRUCache(1)
    lru.put(2, 1)
    assert lru.get(2) == 1
    lru.put(3, 2)
    assert lru.get(2) == -1
    assert lru.get(3) == 2
    print("Test case 2 passed")

    # Test case 3: Multiple operations
    lru = LRUCache(3)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    lru.put(4, 4)
    assert lru.get(4) == 4
    assert lru.get(3) == 3
    assert lru.get(2) == 2
    assert lru.get(1) == -1
    lru.put(5, 5)
    assert lru.get(1) == -1
    assert lru.get(2) == 2
    assert lru.get(3) == 3
    assert lru.get(4) == -1
    assert lru.get(5) == 5
    print("Test case 3 passed")

test_lru_cache()
```

### Time and Space Complexity Analysis
- **Time Complexity**:
  - `get(key)`: O(1) - Accessing the hash map and moving a node to the head are both O(1).
  - `put(key, value)`: O(1) - Updating the hash map and adding/moving nodes in the linked list are O(1). Evicting the tail node is also O(1).
- **Space Complexity**: O(capacity) - The hash map and linked list store at most `capacity` elements.

### Test Cases
The provided test cases verify:
1. Basic functionality (insertion, retrieval, eviction).
2. Edge case with capacity 1.
3. Multiple operations to ensure the LRU property is maintained.

This ensures the solution handles typical scenarios and edge cases correctly.