def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test cases
test1 = ["h","e","l","l","o"]
reverseString(test1)
print(test1)  # Output: ["o","l","l","e","h"]

test2 = ["H","a","n","n","a","h"]
reverseString(test2)
print(test2)  # Output: ["h","a","n","n","a","H"]

test3 = ["a"]
reverseString(test3)
print(test3)  # Output: ["a"]

test4 = ["a", "b"]
reverseString(test4)
print(test4)  # Output: ["b", "a"]
