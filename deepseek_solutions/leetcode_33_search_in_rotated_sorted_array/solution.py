def search(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Else the right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# Test cases
print(search([4,5,6,7,0,1,2], 0))  # Output: 4
print(search([4,5,6,7,0,1,2], 3))  # Output: -1
print(search([1], 0))               # Output: -1
print(search([1,3], 3))             # Output: 1
print(search([5,1,3], 5))           # Output: 0
