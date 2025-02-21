import heapq
from collections import defaultdict
from typing import List, Dict

class Record:
    def __init__(self, id: int, score: int):
        self.id = id
        self.score = score

def high_five(records: List[Record]) -> Dict[int, float]:
    """
    计算每个学生最高5个分数的平均值
    :param records: List[Record]，学生ID和分数的记录列表
    :return: Dict[int, float]，学生ID到平均分的映射
    """
    # 使用默认字典存储每个学生的最小堆（保持最高的5个分数）
    scores = defaultdict(list)
    
    # 处理每条记录
    for record in records:
        # 使用最小堆保持最高的5个分数
        heapq.heappush(scores[record.id], record.score)
        # 如果堆大小超过5，弹出最小的分数
        if len(scores[record.id]) > 5:
            heapq.heappop(scores[record.id])
    
    # 计算每个学生的平均分
    result = {}
    for student_id, top_scores in scores.items():
        # 确保学生有至少5个分数
        if len(top_scores) == 5:
            result[student_id] = sum(top_scores) / 5.0
    
    return result

def test_high_five():
    # 测试用例1：基本情况
    records1 = [
        Record(1, 95), Record(1, 95), Record(1, 91), 
        Record(1, 91), Record(1, 93), Record(1, 90),
        Record(2, 85), Record(2, 90), Record(2, 80), 
        Record(2, 85), Record(2, 88)
    ]
    result1 = high_five(records1)
    expected1 = {1: 93.0, 2: 85.6}  # (95+95+93+91+91)/5, (90+88+85+85+80)/5
    assert abs(result1[1] - expected1[1]) < 0.001, \
        f"Expected {expected1[1]}, but got {result1[1]} for student 1"
    assert abs(result1[2] - expected1[2]) < 0.001, \
        f"Expected {expected1[2]}, but got {result1[2]} for student 2"
    
    # 测试用例2：学生成绩不足5个
    records2 = [
        Record(1, 95), Record(1, 95), Record(1, 91), Record(1, 91)
    ]
    result2 = high_five(records2)
    assert 1 not in result2, "Student with less than 5 scores should not be included"
    
    # 测试用例3：多个学生，部分学生成绩不足
    records3 = [
        Record(1, 95), Record(1, 95), Record(1, 91), 
        Record(1, 91), Record(1, 93),
        Record(2, 85), Record(2, 90), Record(2, 80), 
        Record(3, 85), Record(3, 90)
    ]
    result3 = high_five(records3)
    assert len(result3) == 1, "Only student 1 should have average"
    assert abs(result3[1] - 93.0) < 0.001, \
        f"Expected 93.0, but got {result3[1]} for student 1"
    
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_high_five() 