# Missing Number

## Problem Description

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

## Examples

**Example 1:**
```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

**Example 2:**
```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
```

**Example 3:**
```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```

## Constraints

- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

## Approach

### Approach 1: Sorting

#### English

This approach sorts the array and then checks each index against its value. Since the array should contain numbers from 0 to n (except one missing number), after sorting, each number should match its index. The first position where this doesn't happen is the missing number.

1. Sort the array.
2. Iterate through the array, checking if each index matches its value.
3. If there's a mismatch, return that index.
4. If we complete the iteration without finding a mismatch, then n is the missing number (since the array contains numbers from 0 to n-1).

Time Complexity: O(n log n) due to sorting.
Space Complexity: O(1) or O(n) depending on the sorting algorithm used.

#### Chinese

这种方法首先对数组进行排序，然后检查每个索引与其值是否匹配。由于数组应该包含从0到n的数字（除了一个缺失的数字），排序后，每个数字应该与其索引匹配。第一个不匹配的位置就是缺失的数字。

1. 对数组进行排序。
2. 遍历数组，检查每个索引是否与其值匹配。
3. 如果有不匹配，返回该索引。
4. 如果我们完成遍历而没有找到不匹配，那么n就是缺失的数字（因为数组包含从0到n-1的数字）。

时间复杂度：O(n log n)，这是由于排序所需的时间。
空间复杂度：O(1)或O(n)，取决于所使用的排序算法。

### Approach 2: Mathematical Approach

#### English

This approach uses the formula for the sum of an arithmetic series to find the missing number.

1. Calculate the expected sum of numbers from 0 to n: `n * (n + 1) / 2`.
2. Calculate the actual sum of the array.
3. The difference between the expected and actual sum is the missing number.

Time Complexity: O(n)
Space Complexity: O(1)

#### Chinese

这种方法使用等差数列求和公式来找出缺失的数字。

1. 计算从0到n的数字的预期总和：`n * (n + 1) / 2`。
2. 计算数组的实际总和。
3. 预期总和与实际总和之间的差值就是缺失的数字。

时间复杂度：O(n)
空间复杂度：O(1)

### Approach 3: XOR Approach

#### English

This approach uses the properties of XOR operations.

1. Initialize a variable `result` with n.
2. For each index i in the array, XOR `result` with both i and nums[i].
3. The final value of `result` will be the missing number.

This works because:
- XORing a number with itself results in 0.
- XORing a number with 0 gives the number itself.
- XOR is commutative and associative.

When we XOR all numbers from 0 to n (including n) and all elements in the array, all numbers except the missing one will be XORed exactly twice (once as an index and once as a value), canceling out to 0. The missing number will be XORed only once, leaving it as the final result.

Time Complexity: O(n)
Space Complexity: O(1)

#### Chinese

这种方法利用了XOR操作的特性。

1. 用n初始化一个变量`result`。
2. 对于数组中的每个索引i，将`result`与i和nums[i]进行XOR操作。
3. `result`的最终值将是缺失的数字。

这样做的原理是：
- 一个数与自身进行XOR操作，结果为0。
- 一个数与0进行XOR操作，得到的是数本身。
- XOR是可交换的和可结合的。

当我们对0到n（包括n）的所有数字和数组中的所有元素进行XOR操作时，除了缺失的数字外，所有数字都会被XOR操作两次（一次作为索引，一次作为值），相互抵消为0。缺失的数字只会被XOR操作一次，留下它作为最终结果。

时间复杂度：O(n)
空间复杂度：O(1) 