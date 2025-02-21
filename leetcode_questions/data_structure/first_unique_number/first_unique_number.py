from collections import OrderedDict

class DataStream:
    """
    处理数据流，找到第一个唯一数字
    使用OrderedDict保持插入顺序
    """
    def __init__(self):
        self.counter = {}  # 计数器
        self.unique_nums = OrderedDict()  # 保持顺序的唯一数字
    
    def add(self, num):
        """
        添加数字到数据流
        :param num: int，新的数字
        """
        # 更新计数
        self.counter[num] = self.counter.get(num, 0) + 1
        
        if self.counter[num] == 1:
            # 第一次出现，添加到唯一数字集合
            self.unique_nums[num] = None
        elif num in self.unique_nums:
            # 不再唯一，从唯一数字集合中移除
            del self.unique_nums[num]
    
    def first_unique(self):
        """
        获取数据流中的第一个唯一数字
        :return: int，第一个唯一数字，如果不存在返回-1
        """
        if not self.unique_nums:
            return -1
        return next(iter(self.unique_nums))

def first_unique_number(nums, target):
    """
    在数据流中找到终止数字出现时的第一个唯一数字
    :param nums: List[int]，数据流
    :param target: int，终止数字
    :return: int，第一个唯一数字，如果找不到返回-1
    """
    stream = DataStream()
    
    for num in nums:
        stream.add(num)
        if num == target:
            return stream.first_unique()
            
    return -1  # 没有找到终止数字

def test_first_unique_number():
    # 测试用例1：基本情况
    nums1 = [1, 2, 2, 1, 3, 4, 4, 5]
    target1 = 5
    assert first_unique_number(nums1, target1) == 3, \
        f"Expected 3, but got {first_unique_number(nums1, target1)}"
    
    # 测试用例2：没有唯一数字
    nums2 = [1, 1, 2, 2, 3, 3]
    target2 = 3
    assert first_unique_number(nums2, target2) == -1, \
        f"Expected -1, but got {first_unique_number(nums2, target2)}"
    
    # 测试用例3：终止数字不存在
    nums3 = [1, 2, 3]
    target3 = 4
    assert first_unique_number(nums3, target3) == -1, \
        f"Expected -1, but got {first_unique_number(nums3, target3)}"
    
    # 测试用例4：终止数字是第一个唯一数字
    nums4 = [1, 2, 2, 1, 3]
    target4 = 3
    assert first_unique_number(nums4, target4) == 3, \
        f"Expected 3, but got {first_unique_number(nums4, target4)}"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_first_unique_number() 