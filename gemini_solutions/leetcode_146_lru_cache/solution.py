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