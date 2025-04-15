# Two Sum - All Pairs

## Problem Description
Given an array of integers `nums` and an integer `target`, find all pairs of numbers such that they add up to `target`.

Unlike the original Two Sum problem, this variation:
1. Returns the actual values (not indices)
2. Finds all possible pairs (not just one solution)
3. Handles duplicate numbers appropriately

## Examples

### Example 1:
```
Input: nums = [1,2,3,4,5], target = 6
Output: [[1,5], [2,4]]
Explanation: Both 1+5=6 and 2+4=6, so we return both pairs.
```

### Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [[2,4]]
Explanation: Only 2+4=6, so we return this pair.
```

### Example 3:
```
Input: nums = [3,3], target = 6
Output: [[3,3]]
Explanation: The only possible pair is 3+3=6.
```

### Example 4:
```
Input: nums = [-1,-2,-3,-4,-5], target = -8
Output: [[-5,-3], [-4,-4]]
Explanation: Both -5+-3=-8 and -4+-4=-8.
```

## Constraints
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

## Solution Approaches

### 1. Brute Force Approach
The most straightforward approach is to check all possible pairs of numbers in the array.

**Algorithm:**
1. Initialize an empty result array
2. Use two nested loops to iterate through each pair of elements
3. If a pair sums to the target, add it to the result
4. Return all found pairs

**Time Complexity:** O(n²) - We check n*(n-1)/2 pairs in the worst case
**Space Complexity:** O(k) - Where k is the number of pairs found

### 2. Two-Pass Hash Table
We can improve the time complexity by using a hash table.

**Algorithm:**
1. Create a hash map to store each element and its indices (to handle duplicates)
2. Fill the hash map in the first pass
3. In the second pass, check if the complement (target - current number) exists in the hash map
4. Add each unique pair to the result, avoiding duplicates using a set
5. Return all found pairs

**Time Complexity:** O(n) - We make two passes through the array
**Space Complexity:** O(n + k) - We use additional space for the hash map and result

### 3. One-Pass Hash Table
We can further optimize by checking for complements while iterating.

**Algorithm:**
1. Initialize an empty result array and sets for seen numbers and seen pairs
2. Iterate through the array in a single pass
3. For each element:
   - Calculate the complement (target - current number)
   - If the complement is in the seen set and the pair hasn't been added yet, add it to the result
   - Add the current number to the seen set
4. Return all found pairs

**Time Complexity:** O(n) - We make one pass through the array
**Space Complexity:** O(n + k) - We use additional space for the sets and result

### 4. Two-Pointer Approach
This approach sorts the array first and then uses two pointers to find pairs.

**Algorithm:**
1. Sort the input array
2. Initialize an empty result array and a set for seen pairs
3. Place pointers at the beginning and end of the array
4. While the left pointer is less than the right pointer:
   - If the sum equals the target, add the pair to the result and move both pointers
   - If the sum is less than the target, move the left pointer
   - If the sum is greater than the target, move the right pointer
5. Return all found pairs

**Time Complexity:** O(n log n) - Dominated by the sorting operation
**Space Complexity:** O(k) - For storing the result, where k is the number of pairs found

## Follow-up
Can you come up with an algorithm that is less than O(n²) time complexity?

The hash map approaches (methods 2 and 3) achieve O(n) time complexity, which is better than the naive O(n²) solution. 