import random

class RandomizedCollection:
    """
    支持重复元素的插入、删除和随机获取的数据结构
    所有操作的期望时间复杂度为 O(1)
    """
    def __init__(self):
        self.nums = []  # 存储所有数字的列表
        self.index_map = {}  # 值到索引集合的映射 {val -> set(indices)}
        
    def insert(self, val):
        """
        插入一个值
        :param val: 要插入的值
        :return: bool，如果该值之前不存在则返回True
        """
        # 获取返回值（之前是否存在）
        is_new = val not in self.index_map
        
        # 如果是新值，初始化索引集合
        if is_new:
            self.index_map[val] = set()
            
        # 将值添加到列表末尾，并记录其索引
        self.index_map[val].add(len(self.nums))
        self.nums.append(val)
        
        return is_new
        
    def remove(self, val):
        """
        删除一个值
        :param val: 要删除的值
        :return: bool，如果该值存在则返回True
        """
        if val not in self.index_map:
            return False
            
        # 获取要删除的值的一个索引
        remove_idx = self.index_map[val].pop()
        last_val = self.nums[-1]
        
        # 如果要删除的不是最后一个元素
        if remove_idx < len(self.nums) - 1:
            # 将最后一个元素移到要删除的位置
            self.nums[remove_idx] = last_val
            self.index_map[last_val].remove(len(self.nums) - 1)
            self.index_map[last_val].add(remove_idx)
            
        # 删除最后一个元素
        self.nums.pop()
        
        # 如果该值的所有实例都被删除，移除映射
        if not self.index_map[val]:
            del self.index_map[val]
            
        return True
        
    def getRandom(self):
        """
        随机获取一个元素
        :return: 随机元素
        """
        return random.choice(self.nums)

def test_randomized_collection():
    # 测试用例1：基本操作
    collection = RandomizedCollection()
    assert collection.insert(1) == True
    assert collection.insert(1) == False  # 已存在
    assert collection.insert(2) == True
    
    # 验证随机性（简单测试）
    results = set()
    for _ in range(10):
        results.add(collection.getRandom())
    assert results <= {1, 2}  # 结果应该是{1, 2}的子集
    
    # 测试删除
    assert collection.remove(1) == True
    assert collection.remove(1) == True
    assert collection.remove(1) == False  # 已经没有1了
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_randomized_collection() 