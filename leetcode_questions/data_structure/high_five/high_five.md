# High Five

## 题目描述
有一组学生的成绩记录，每个记录包含学生ID和分数。对于每个学生，计算他们最高的5个分数的平均值。

要求：
1. 每个学生至少要有5个分数才计算平均值
2. 返回所有符合条件的学生的平均分
3. 平均分保留一位小数

## 示例
输入: 
```python
[
    (1, 95), (1, 95), (1, 91), (1, 91), (1, 93),
    (2, 85), (2, 90), (2, 80), (2, 85), (2, 88)
]
```
输出: 
```python
{
    1: 93.0,  # (95 + 95 + 93 + 91 + 91) / 5
    2: 85.6   # (90 + 88 + 85 + 85 + 80) / 5
}
```

## 解题思路

### 数据结构选择
1. **最小堆**
   - 用于维护每个学生的最高5个分数
   - 当有新分数时，只保留最高的5个

2. **哈希表**
   - 映射学生ID到其分数堆
   - 方便按学生分组处理分数

### 实现细节

1. **维护最高分**
   - 使用最小堆保持最高的5个分数
   - 堆大小超过5时，弹出最小值
   - Python的heapq模块提供了堆操作

2. **计算平均值**
   - 确保学生有至少5个分数
   - 对堆中的5个分数求和取平均

### 复杂度分析
- 时间复杂度：O(nlogk)
  - n是记录总数
  - k是保留的分数数量（这里是5）
  - 每次堆操作是O(logk)
- 空间复杂度：O(m*k)
  - m是学生数量
  - k是每个学生保留的分数数量

## 代码实现要点
1. 使用defaultdict避免键检查
2. 正确处理堆的大小限制
3. 处理成绩不足5个的情况
4. 注意浮点数计算的精度

## 优化可能
1. 如果数据量很大，可以考虑批处理
2. 可以使用固定大小的数组代替堆（因为只需要5个元素）
3. 可以在插入时就计算部分和，减少最后计算的工作 