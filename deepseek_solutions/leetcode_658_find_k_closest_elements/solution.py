def findClosestElements(arr, k, x):
    left = 0
    right = len(arr) - k
    
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]

# Test cases
test1 = [1,2,3,4,5]
k1 = 4
x1 = 3
print(findClosestElements(test1, k1, x1))  # Output: [1,2,3,4]

test2 = [1,2,3,4,5]
k2 = 4
x2 = -1
print(findClosestElements(test2, k2, x2))  # Output: [1,2,3,4]

test3 = [1,1,1,10,10,10]
k3 = 1
x3 = 9
print(findClosestElements(test3, k3, x3))  # Output: [10]

test4 = [1,3,6,7,8]
k4 = 3
x4 = 5
print(findClosestElements(test4, k4, x4))  # Output: [3,6,7]
