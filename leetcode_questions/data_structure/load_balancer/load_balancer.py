import random
from typing import List, Optional

class Server:
    """服务器节点"""
    def __init__(self, server_id: int):
        self.id = server_id
        self.next = None
        self.prev = None

class LoadBalancer:
    """
    负载均衡器实现
    使用双向链表 + 哈希表实现O(1)的增删改查
    """
    def __init__(self):
        self.servers = {}  # server_id -> Server节点
        # 使用虚拟头尾节点简化操作
        self.head = Server(-1)  # 虚拟头节点
        self.tail = Server(-1)  # 虚拟尾节点
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add(self, server_id: int) -> None:
        """
        添加服务器
        :param server_id: int，服务器ID
        """
        if server_id in self.servers:
            return
        
        # 创建新节点
        new_server = Server(server_id)
        self.servers[server_id] = new_server
        
        # 添加到链表尾部
        prev = self.tail.prev
        prev.next = new_server
        new_server.prev = prev
        new_server.next = self.tail
        self.tail.prev = new_server
        
        self.size += 1
    
    def remove(self, server_id: int) -> bool:
        """
        移除服务器
        :param server_id: int，服务器ID
        :return: bool，是否成功移除
        """
        if server_id not in self.servers:
            return False
        
        # 从链表中移除
        server = self.servers[server_id]
        server.prev.next = server.next
        server.next.prev = server.prev
        
        # 从哈希表中移除
        del self.servers[server_id]
        self.size -= 1
        return True
    
    def pick(self) -> Optional[int]:
        """
        随机选择一个服务器
        :return: int，选中的服务器ID，如果没有服务器返回None
        """
        if not self.size:
            return None
        
        # 随机选择一个索引
        index = random.randint(0, self.size - 1)
        
        # 遍历到选中的位置
        current = self.head.next
        for _ in range(index):
            current = current.next
            
        return current.id

def test_load_balancer():
    # 测试用例1：基本操作
    lb = LoadBalancer()
    
    # 测试添加服务器
    lb.add(1)
    lb.add(2)
    lb.add(3)
    assert len(lb.servers) == 3, "Should have 3 servers"
    
    # 测试随机选择
    selected = set()
    for _ in range(30):  # 多次选择以验证随机性
        server_id = lb.pick()
        assert server_id in {1, 2, 3}, f"Invalid server id: {server_id}"
        selected.add(server_id)
    assert len(selected) == 3, "Should be able to select all servers"
    
    # 测试移除服务器
    assert lb.remove(2) == True, "Should successfully remove server 2"
    assert lb.remove(2) == False, "Should fail to remove non-existent server"
    assert len(lb.servers) == 2, "Should have 2 servers remaining"
    
    # 测试重复添加
    lb.add(1)  # 添加已存在的服务器
    assert len(lb.servers) == 2, "Should not add duplicate server"
    
    # 测试空负载均衡器
    lb2 = LoadBalancer()
    assert lb2.pick() is None, "Empty balancer should return None"
    assert lb2.remove(1) == False, "Should not remove from empty balancer"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_load_balancer() 