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
