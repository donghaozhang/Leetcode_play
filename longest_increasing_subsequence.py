#!/usr/bin/env python

def longest_increasing_subsequence(nums):
    """Return the longest increasing subsequence from the list of numbers."""
    if not nums:
        return []
    n = len(nums)
    # dp[i] will be the length of the subsequence ending at index i
    dp = [1] * n
    # prev[i] will store the index of the previous element in the subsequence
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the index of the maximum value in dp
    max_index = 0
    for i in range(n):
        if dp[i] > dp[max_index]:
            max_index = i

    # Reconstruct the subsequence using prev array
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]
    lis.reverse()
    return lis


if __name__ == '__main__':
    # Example usage
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    lis = longest_increasing_subsequence(nums)
    print("Input sequence:", nums)
    print("Longest increasing subsequence:", lis)
    print("Length of subsequence:", len(lis)) 