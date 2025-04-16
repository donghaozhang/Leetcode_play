from typing import List

class Solution:
    def get_next_chunk(self, version: str, n: int, p: int) -> List[int]:
        # If pointer is set to the end of the string, return 0
        if p > n - 1:
            return 0, p

        # Find the end of the chunk
        p_end = p
        while p_end < n and version[p_end] != ".":
            p_end += 1

        # Retrieve the chunk
        i = int(version[p:p_end]) if p_end != n - 1 else int(version[p:n])

        # Find the beginning of the next chunk
        p = p_end + 1

        return i, p

    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)

        # Compare versions
        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)
            if i1 != i2:
                return 1 if i1 > i2 else -1

        # The versions are equal
        return 0
    
    # Alternative simpler approach using split
    def compareVersion_simple(self, version1: str, version2: str) -> int:
        v1_parts = list(map(int, version1.split('.')))
        v2_parts = list(map(int, version2.split('.')))
        
        # Make both lists the same length by adding zeros
        max_length = max(len(v1_parts), len(v2_parts))
        v1_parts.extend([0] * (max_length - len(v1_parts)))
        v2_parts.extend([0] * (max_length - len(v2_parts)))
        
        # Compare parts
        for i in range(max_length):
            if v1_parts[i] > v2_parts[i]:
                return 1
            elif v1_parts[i] < v2_parts[i]:
                return -1
                
        return 0

# Test cases
def test_compare_version():
    solution = Solution()
    
    # Test case 1
    version1_1 = "1.2"
    version2_1 = "1.10"
    print(f"Input: version1 = \"{version1_1}\", version2 = \"{version2_1}\"")
    print(f"Output (Chunk method): {solution.compareVersion(version1_1, version2_1)}")
    print(f"Output (Simple method): {solution.compareVersion_simple(version1_1, version2_1)}")
    print(f"Expected: -1")
    print(f"Explanation: version1's second revision is \"2\" and version2's second revision is \"10\": 2 < 10, so version1 < version2.")
    print()
    
    # Test case 2
    version1_2 = "1.01"
    version2_2 = "1.001"
    print(f"Input: version1 = \"{version1_2}\", version2 = \"{version2_2}\"")
    print(f"Output (Chunk method): {solution.compareVersion(version1_2, version2_2)}")
    print(f"Output (Simple method): {solution.compareVersion_simple(version1_2, version2_2)}")
    print(f"Expected: 0")
    print(f"Explanation: Ignoring leading zeroes, both \"01\" and \"001\" represent the same integer \"1\".")
    print()
    
    # Test case 3
    version1_3 = "1.0"
    version2_3 = "1.0.0.0"
    print(f"Input: version1 = \"{version1_3}\", version2 = \"{version2_3}\"")
    print(f"Output (Chunk method): {solution.compareVersion(version1_3, version2_3)}")
    print(f"Output (Simple method): {solution.compareVersion_simple(version1_3, version2_3)}")
    print(f"Expected: 0")
    print(f"Explanation: version1 has less revisions, which means every missing revision are treated as \"0\".")
    print()
    
    # Test case 4 - version1 > version2
    version1_4 = "2.0.1"
    version2_4 = "1.9.9.9"
    print(f"Input: version1 = \"{version1_4}\", version2 = \"{version2_4}\"")
    print(f"Output (Chunk method): {solution.compareVersion(version1_4, version2_4)}")
    print(f"Output (Simple method): {solution.compareVersion_simple(version1_4, version2_4)}")
    print(f"Expected: 1")
    print(f"Explanation: 2.0.1 > 1.9.9.9 since 2 > 1 in the first revision.")

if __name__ == "__main__":
    test_compare_version() 