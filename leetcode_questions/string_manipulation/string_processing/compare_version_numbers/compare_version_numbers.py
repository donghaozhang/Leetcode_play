from typing import List

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Compare two version numbers version1 and version2.
        
        Args:
            version1: A string representing the first version number
            version2: A string representing the second version number
            
        Returns:
            1 if version1 > version2
            -1 if version1 < version2
            0 if version1 == version2
        """
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


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: version1 > version2
    version1 = "1.01"
    version2 = "1.001"
    print(f"Comparing {version1} and {version2}: {solution.compareVersion(version1, version2)}")  # Expected: 0
    
    # Test case 2: version1 < version2
    version1 = "1.0"
    version2 = "1.0.0"
    print(f"Comparing {version1} and {version2}: {solution.compareVersion(version1, version2)}")  # Expected: 0
    
    # Test case 3: version1 == version2
    version1 = "0.1"
    version2 = "1.1"
    print(f"Comparing {version1} and {version2}: {solution.compareVersion(version1, version2)}")  # Expected: -1
    
    # Test case 4: Leading zeros and different lengths
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    print(f"Comparing {version1} and {version2}: {solution.compareVersion(version1, version2)}")  # Expected: -1 