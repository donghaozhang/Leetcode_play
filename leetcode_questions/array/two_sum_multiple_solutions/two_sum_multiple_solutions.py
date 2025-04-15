from typing import List, Tuple

class TwoSumSolutions:
    """
    Class containing multiple solution approaches for the Two Sum - All Pairs problem
    
    This variant finds all pairs of values (not indices) that sum to the target.
    For example, with nums = [1,2,3,4,5] and target = 6, return [[1,5], [2,4]]
    """
    
    @staticmethod
    def brute_force(nums: List[int], target: int) -> List[List[int]]:
        """
        Brute force approach - check all pairs
        Time Complexity: O(n²)
        Space Complexity: O(k) where k is the number of pairs found
        """
        n = len(nums)
        result = []
        seen_pairs = set()  # To avoid duplicate pairs
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    # Always store pairs with smaller value first
                    pair = sorted([nums[i], nums[j]])
                    pair_tuple = tuple(pair)
                    if pair_tuple not in seen_pairs:
                        result.append(pair)
                        seen_pairs.add(pair_tuple)
        return result
    
    @staticmethod
    def two_pass_hash_table(nums: List[int], target: int) -> List[List[int]]:
        """
        Two-pass hash table approach
        Time Complexity: O(n)
        Space Complexity: O(n + k) where k is the number of pairs found
        """
        # First pass: build the hash map
        value_indices = {}
        for i, num in enumerate(nums):
            if num in value_indices:
                value_indices[num].append(i)
            else:
                value_indices[num] = [i]
        
        # Second pass: find all pairs
        result = []
        seen_pairs = set()  # To avoid duplicate pairs
        
        for num in nums:
            complement = target - num
            if complement in value_indices:
                # Make sure we're not using the same element twice
                # and haven't already included this pair
                pair = tuple(sorted([num, complement]))
                if (num != complement or len(value_indices[num]) > 1) and pair not in seen_pairs:
                    result.append(list(pair))
                    seen_pairs.add(pair)
        
        return result
    
    @staticmethod
    def one_pass_hash_table(nums: List[int], target: int) -> List[List[int]]:
        """
        One-pass hash table approach
        Time Complexity: O(n)
        Space Complexity: O(n + k) where k is the number of pairs found
        """
        seen = set()
        result = []
        seen_pairs = set()  # To avoid duplicate pairs
        
        for num in nums:
            complement = target - num
            if complement in seen and tuple(sorted([num, complement])) not in seen_pairs:
                pair = tuple(sorted([num, complement]))
                result.append(list(pair))
                seen_pairs.add(pair)
            seen.add(num)
        
        return result
    
    @staticmethod
    def two_pointer(nums: List[int], target: int) -> List[List[int]]:
        """
        Two-pointer approach (requires sorting)
        Time Complexity: O(n log n)
        Space Complexity: O(k) where k is the number of pairs found
        """
        # Sort the array
        sorted_nums = sorted(nums)
        result = []
        seen_pairs = set()  # To avoid duplicate pairs
        
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = sorted_nums[left] + sorted_nums[right]
            
            if current_sum == target:
                # Always ensure consistent ordering of pairs
                pair = (sorted_nums[left], sorted_nums[right])
                if pair not in seen_pairs:
                    result.append([sorted_nums[left], sorted_nums[right]])
                    seen_pairs.add(pair)
                # Move both pointers to find more pairs
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:  # current_sum > target
                right -= 1
        
        return result


def test_all_solutions():
    """
    Test all solution approaches with multiple test cases
    """
    solutions = TwoSumSolutions()
    solution_methods = [
        ("Brute Force", solutions.brute_force),
        ("Two-Pass Hash Table", solutions.two_pass_hash_table),
        ("One-Pass Hash Table", solutions.one_pass_hash_table),
        ("Two-Pointer (Sorted)", solutions.two_pointer)
    ]
    
    test_cases = [
        {
            "nums": [2, 7, 11, 15], 
            "target": 9, 
            "expected": [[2, 7]]
        },
        {
            "nums": [3, 2, 4], 
            "target": 6, 
            "expected": [[2, 4]]
        },
        {
            "nums": [3, 3], 
            "target": 6, 
            "expected": [[3, 3]]
        },
        {
            "nums": [1, 2, 3, 4, 5], 
            "target": 6,
            "expected": [[1, 5], [2, 4]]
        },
        {
            "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
            "target": 11,
            "expected": [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]
        },
        {
            "nums": [-1, -2, -3, -4, -5], 
            "target": -8, 
            "expected": [[-5, -3]]
        },
        {
            "nums": [1, 1, 1, 2, 2, 3, 3], 
            "target": 4, 
            "expected": [[1, 3], [2, 2]]
        }
    ]
    
    for method_name, method in solution_methods:
        print(f"\nTesting {method_name} approach:")
        
        for i, tc in enumerate(test_cases):
            nums = tc["nums"]
            target = tc["target"]
            result = method(nums, target)
            
            # Make a copy of the expected result to avoid modifying the original
            expected = [list(pair) for pair in tc["expected"]]
            
            # Sort each pair and then sort the list of pairs for consistent comparison
            result_sorted = sorted([sorted(pair) for pair in result])
            expected_sorted = sorted([sorted(pair) for pair in expected])
            
            assert result_sorted == expected_sorted, f"Test case {i+1} failed: Expected {expected_sorted}, got {result_sorted}"
            print(f"  Test case {i+1}: Passed ✓ - Found pairs {result}")
    
    print("\nAll solution approaches passed all test cases! ✓")


if __name__ == "__main__":
    test_all_solutions() 