# 寻找峰值元素

## 题目描述
峰值元素是指其值大于左右相邻值的元素。给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

## 示例
输入: nums = [1,2,1,3,5,6,4]
输出: 5
解释: 6 是峰值元素，返回其索引 5

## 解题思路

### 二分查找策略
1. **初始化**
   - 设置左右指针
   - 使用二分模板

2. **查找规则**
   - 比较中间元素与其右邻居
   - 如果中间元素小于右邻居，峰值在右半部分
   - 否则峰值在左半部分或就是中间元素

3. **终止条件**
   - 当左右指针相邻时停止
   - 返回较大值的索引

### 为什么这样做是对的？
- 如果 nums[i] < nums[i+1]，那么在 i 的右边一定存在峰值
- 如果 nums[i] > nums[i+1]，那么在 i 的左边一定存在峰值
- 这个性质保证了二分查找的正确性

### 复杂度分析
- 时间复杂度：O(log n)
- 空间复杂度：O(1)

## 代码实现要点
1. 正确处理边界条件
2. 注意数组为空的情况
3. 处理只有一个或两个元素的数组
4. 正确比较相邻元素

## 常见错误
1. 忘记处理边界情况
2. 二分查找的条件写错
3. 返回值的选择错误
4. 没有考虑数组长度为1的情况

## 相关题目
1. 寻找山峰数组的峰顶索引
2. 寻找最接近的元素
3. 寻找旋转排序数组中的最小值 