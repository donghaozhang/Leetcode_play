# Compare Version Numbers

## Problem Description

Given two version numbers, `version1` and `version2`, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on.

For example, `2.5.33` and `0.1` are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions `1` and `001` are considered equal. If a version number does not specify a revision at an index, then treat the revision as `0`. For example, version `1.0` is less than version `1.1` because their revision 0s are the same, but their revision 1s are `0` and `1` respectively, and `0 < 1`.

Return the following:
- If `version1 < version2`, return `-1`.
- If `version1 > version2`, return `1`.
- Otherwise, return `0`.

## Examples

**Example 1:**
```
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeros, both "01" and "001" represent the same integer "1".
```

**Example 2:**
```
Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".
```

**Example 3:**
```
Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
```

## Constraints
- `1 <= version1.length, version2.length <= 500`
- `version1` and `version2` only contain digits and `'.'`
- `version1` and `version2` are valid version numbers
- All revisions in `version1` and `version2` can be stored in a 32-bit integer

## Solution Approach

1. Split both version strings by the dot character to get a list of revision numbers.
2. Convert each revision to an integer (this automatically removes leading zeros).
3. Make both lists the same length by padding the shorter list with zeros.
4. Compare each pair of revisions from left to right.
5. Return the appropriate result based on the comparison.

### Time Complexity
O(max(n, m)) where n and m are the lengths of the version strings.

### Space Complexity
O(max(n, m)) for storing the split version strings.

## Python Solution

```python
def compareVersion(version1: str, version2: str) -> int:
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    
    # Make both lists the same length by padding with zeros
    max_length = max(len(v1_parts), len(v2_parts))
    v1_parts.extend([0] * (max_length - len(v1_parts)))
    v2_parts.extend([0] * (max_length - len(v2_parts)))
    
    # Compare each revision number
    for i in range(max_length):
        if v1_parts[i] > v2_parts[i]:
            return 1
        elif v1_parts[i] < v2_parts[i]:
            return -1
    
    # If we get here, versions are equal
    return 0
```

## Alternative Approach

An alternative approach is to compare the revisions one by one without first padding the arrays:

```python
def compareVersion(version1: str, version2: str) -> int:
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    
    for i in range(max(len(v1_parts), len(v2_parts))):
        # Get revision numbers, defaulting to 0 if index is out of bounds
        v1 = v1_parts[i] if i < len(v1_parts) else 0
        v2 = v2_parts[i] if i < len(v2_parts) else 0
        
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
    
    return 0
```

This solution avoids allocating extra space for padding but achieves the same result. 