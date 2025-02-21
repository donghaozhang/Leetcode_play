class Node:
    """双向链表节点"""
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    LRU (Least Recently Used) 缓存实现
    使用哈希表 + 双向链表
    """
    def __init__(self, capacity):
        """
        初始化 LRU 缓存
        :param capacity: int，缓存容量
        """
        self.capacity = capacity
        self.cache = {}  # 哈希表：key -> Node
        
        # 创建虚拟头尾节点
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        """在头部添加节点（最近使用）"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """移除节点"""
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    
    def _move_to_head(self, node):
        """将节点移动到头部"""
        self._remove_node(node)
        self._add_node(node)
    
    def get(self, key):
        """
        获取缓存值
        :param key: 键
        :return: 值，如果不存在返回-1
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)  # 更新为最近使用
            return node.value
        return -1
    
    def put(self, key, value):
        """
        放入缓存
        :param key: 键
        :param value: 值
        """
        if key in self.cache:
            # 更新已存在的节点
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # 创建新节点
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # 如果超出容量，删除最久未使用的节点（尾部）
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]

def test_lru_cache():
    # 测试用例1：基本操作
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # 2被淘汰
    assert cache.get(2) == -1
    
    # 测试用例2：更新已存在的值
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 2)
    assert cache.get(1) == 2
    
    # 测试用例3：容量为1
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    
    # 测试用例4：访问后更新顺序
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # 1变为最近使用
    cache.put(3, 3)  # 2被淘汰
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_lru_cache() 