def copy_books_binary_search(pages, k):
    """
    二分答案法解决抄书问题
    :param pages: List[int]，每本书的页数
    :param k: int，抄写员人数
    :return: int，最少需要的时间
    """
    if not pages:
        return 0
    if k >= len(pages):
        return max(pages)  # 每人最多抄一本书
        
    def is_feasible(limit):
        """判断在给定时间限制下是否能完成抄写"""
        count = 1  # 当前需要的抄写员数量
        current_sum = 0  # 当前抄写员的工作量
        
        for page in pages:
            if page > limit:  # 单本书超过时间限制
                return False
            if current_sum + page > limit:
                count += 1  # 需要新的抄写员
                current_sum = page
            else:
                current_sum += page
                
        return count <= k
    
    # 二分查找最小的可行时间
    left = max(pages)  # 最小可能的时间（最大页数）
    right = sum(pages)  # 最大可能的时间（所有页数之和）
    
    while left + 1 < right:
        mid = (left + right) // 2
        if is_feasible(mid):
            right = mid  # 尝试更小的时间限制
        else:
            left = mid  # 需要更多时间
            
    return left if is_feasible(left) else right 

# 测试用例
def test_copy_books():
    # 测试用例1: 基本情况
    assert copy_books_binary_search([3, 2, 4], 2) == 5
    # 解释: 第一个人抄前两本书 [3, 2]，花费5分钟；第二个人抄最后一本书 [4]，花费4分钟。最大值是5分钟。
    
    # 测试用例2: 抄写员数量等于书的数量
    assert copy_books_binary_search([1, 2, 3, 4, 5], 5) == 5
    # 解释: 每人抄一本书，最大页数是5
    
    # 测试用例3: 抄写员数量大于书的数量
    assert copy_books_binary_search([1, 2, 3], 5) == 3
    # 解释: 每人最多抄一本书，最大页数是3
    
    # 测试用例4: 空数组
    assert copy_books_binary_search([], 1) == 0
    
    # 测试用例5: 只有一个抄写员
    assert copy_books_binary_search([1, 2, 3, 4, 5], 1) == 15
    # 解释: 一个人抄所有书，总页数是15
    
    # 测试用例6: 更复杂的情况
    assert copy_books_binary_search([3, 2, 4, 1, 5], 3) == 5
    # 可能的分配: [3,2], [4], [1,5] - 最大值是6
    # 或者: [3], [2,4], [1,5] - 最大值是6
    # 最优分配: [3,2], [4,1], [5] - 最大值是5
    
    print("所有测试用例通过!")

if __name__ == "__main__":
    test_copy_books() 