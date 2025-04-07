def permute(nums):
    """
    Generates all permutations of the given list of distinct integers.

    Args:
    nums (list): A list of distinct integers.

    Returns:
    list: A list of lists, where each sublist is a permutation of the input list.
    """
    def backtrack(start, end):
        # If we have filled the permutation, add it to the result
        if start == end:
            result.append(nums[:])  # Use nums[:] to create a copy of nums
        for i in range(start, end):
            # Swap the current number with the start number
            nums[start], nums[i] = nums[i], nums[start]
            # Recur for the remaining numbers
            backtrack(start + 1, end)
            # Backtrack by swapping back
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0, len(nums))
    return result

# Test cases
print(permute([1, 2, 3]))  # Expected: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
print(permute([0, 1]))    # Expected: [[0, 1], [1, 0]]
print(permute([1]))       # Expected: [[1]]
