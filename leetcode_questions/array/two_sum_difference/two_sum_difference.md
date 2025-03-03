# 两数之差

## 题目描述
给定一个排序数组和一个目标值，在数组中找到两个数，使得它们的差等于目标值。返回这两个数的下标。

要求：不使用额外的空间，即空间复杂度为 O(1)。

## 示例
输入: nums = [2, 7, 15, 24], target = 5
输出: [0, 1]
解释: nums[1] - nums[0] = 7 - 2 = 5

## 解题思路

### 双指针法
利用数组的有序性，使用双指针来寻找差值等于目标值的两个数：

1. **预处理**
   - 创建带索引的数组对
   - 按数值排序以便使用双指针

2. **双指针搜索**
   - 初始化左右指针：left = 0, right = 1
   - 计算当前指针指向的数字之差
   - 根据差值调整指针位置：
     - 差值小于目标值：右指针右移
     - 差值大于目标值：左指针右移
     - 差值等于目标值：找到解

3. **指针移动规则**
   - 保持 left < right
   - 当 left 需要移动且会与 right 重合时，同时移动 right

### 为什么这样做是正确的？
- 对于排序后的数组，两数之差随着右指针的移动而增大
- 当差值太小时，需要增大差值，移动右指针
- 当差值太大时，需要减小差值，移动左指针
- 这种单调性保证了算法的正确性

### 复杂度分析
- 时间复杂度：O(nlogn)
  - 排序需要 O(nlogn)
  - 双指针搜索需要 O(n)
- 空间复杂度：O(n)
  - 需要存储带索引的数组
  - 如果要求 O(1) 空间，可以在原数组上操作，但需要还原数组顺序

## 代码实现要点
1. 正确处理带索引的排序
2. 处理负数目标值（取绝对值）
3. 维护左右指针的相对位置
4. 返回原始数组中的索引
5. 处理边界情况（空数组，数组长度不足等） 