# 翻转字符串

## 题目描述
编写一个函数，将输入的字符串进行翻转。

## 示例
输入: "hello"
输出: "olleh"

## 解题思路

### 方法一：双指针
1. **初始化**
   - 将字符串转换为字符数组
   - 设置左右指针分别指向开头和结尾

2. **交换过程**
   - 交换左右指针指向的字符
   - 左指针向右移动，右指针向左移动
   - 直到两个指针相遇

### 方法二：Python切片
- 使用Python的切片特性 `[::-1]` 直接翻转

### 复杂度分析
- 时间复杂度：O(n)
- 空间复杂度：O(n)，需要额外空间存储字符数组

## 代码实现要点
1. 处理空字符串
2. 正确实现字符交换
3. 考虑使用语言特性优化代码

## 相关题目
1. 翻转单词顺序
2. 字符串轮转
3. 反转字符串中的单词 