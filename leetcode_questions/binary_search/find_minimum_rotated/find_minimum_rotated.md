# 旋转排序数组中的最小值

## 题目描述
假设一个按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2]。请找出其中最小的元素。

## 示例
输入: [4, 5, 6, 7, 0, 1, 2]
输出: 0

## 解题思路

### 方法一：基本二分查找
1. **初始化**
   - 设置左右指针
   - 特判：如果数组未旋转，直接返回第一个元素

2. **二分查找**
   - 将中间元素与第一个元素比较
   - 如果中间元素大于第一个元素，说明最小值在右半部分
   - 否则最小值在左半部分或就是中间元素

### 方法二：处理重复元素
1. **初始化**
   - 与基本方法相同
   - 需要处理重复元素的情况

2. **二分查找**
   - 将中间元素与最后一个元素比较
   - 当中间元素等于右边界元素时，无法确定最小值位置
   - 此时可以安全地将右边界左移一位

### 复杂度分析
- 基本方法：
  - 时间复杂度：O(log n)
  - 空间复杂度：O(1)
- 处理重复元素：
  - 时间复杂度：最坏情况 O(n)，平均情况 O(log n)
  - 空间复杂度：O(1)

## 代码实现要点
1. 正确处理未旋转的数组
2. 选择合适的比较元素（首元素或末元素）
3. 处理重复元素的特殊情况
4. 注意边界条件的处理

## 相关题目
1. 搜索旋转排序数组
2. 寻找旋转排序数组中的目标值
3. 寻找峰值元素 