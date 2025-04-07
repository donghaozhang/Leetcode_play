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
