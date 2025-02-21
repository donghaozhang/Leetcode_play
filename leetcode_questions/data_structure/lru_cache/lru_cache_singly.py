class Node:
    """单向链表节点"""
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class LRUCache:
    """
    LRU缓存的单链表实现
    使用哈希表存储前驱节点
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # 键到节点的映射
        self.prev = {}   # 节点到其前驱节点的映射
        self.dummy = Node()  # 虚拟头节点
        self.tail = self.dummy  # 尾节点（最久未使用）
    
    def _add_node(self, node):
        """在头部添加节点"""
        node.next = self.dummy.next
        self.dummy.next = node
        self.prev[node] = self.dummy
        if node.next:
            self.prev[node.next] = node
        if self.tail == self.dummy:
            self.tail = node
    
    def _remove_node(self, node, prev_node):
        """移除节点"""
        prev_node.next = node.next
        if node.next:
            self.prev[node.next] = prev_node
        if node == self.tail:
            self.tail = prev_node
        del self.prev[node]
    
    def _move_to_head(self, node, prev_node):
        """将节点移动到头部"""
        if prev_node == self.dummy:  # 已经在头部
            return
        self._remove_node(node, prev_node)
        self._add_node(node)
    
    def get(self, key):
        """获取缓存值"""
        if key not in self.cache:
            return -1
            
        node = self.cache[key]
        prev_node = self.prev[node]
        self._move_to_head(node, prev_node)
        return node.value
    
    def put(self, key, value):
        """放入缓存"""
        if key in self.cache:
            # 更新已存在的节点
            node = self.cache[key]
            node.value = value
            prev_node = self.prev[node]
            self._move_to_head(node, prev_node)
        else:
            # 创建新节点
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # 如果超出容量，删除最久未使用的节点
            if len(self.cache) > self.capacity:
                lru_node = self.tail
                prev_lru = self.prev[lru_node]
                self._remove_node(lru_node, prev_lru)
                del self.cache[lru_node.key]

def test_lru_cache_singly():
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
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_lru_cache_singly() 