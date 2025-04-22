from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Perform flood fill on the image starting from the given pixel.
        
        Args:
            image: 2D list representing the image
            sr: Starting row index
            sc: Starting column index
            newColor: New color to fill
            
        Returns:
            Modified image after flood fill
        """
        # Get the original color at the starting position
        original_color = image[sr][sc]
        
        # If the new color is same as original, no need to do anything
        if original_color == newColor:
            return image
            
        def dfs(row: int, col: int):
            """
            Depth-first search to fill connected pixels with the same color.
            
            Args:
                row: Current row index
                col: Current column index
            """
            # Check if current pixel has the original color
            if image[row][col] == original_color:
                # Change the color
                image[row][col] = newColor
                
                # Recursively check and fill adjacent pixels
                # Up
                if row > 0:
                    dfs(row - 1, col)
                # Down
                if row < len(image) - 1:
                    dfs(row + 1, col)
                # Left
                if col > 0:
                    dfs(row, col - 1)
                # Right
                if col < len(image[0]) - 1:
                    dfs(row, col + 1)
        
        # Start the flood fill from the given position
        dfs(sr, sc)
        return image

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    image1 = [[1,1,1],[1,1,0],[1,0,1]]
    sr1, sc1, newColor1 = 1, 1, 2
    print(f"Example 1: {solution.floodFill(image1, sr1, sc1, newColor1)}")
    # Expected: [[2,2,2],[2,2,0],[2,0,1]]
    
    # Example 2
    image2 = [[0,0,0],[0,0,0]]
    sr2, sc2, newColor2 = 0, 0, 0
    print(f"Example 2: {solution.floodFill(image2, sr2, sc2, newColor2)}")
    # Expected: [[0,0,0],[0,0,0]]
    
    # Additional test case
    image3 = [[1,1,1],[1,1,1],[1,1,1]]
    sr3, sc3, newColor3 = 0, 0, 2
    print(f"Additional test: {solution.floodFill(image3, sr3, sc3, newColor3)}")
    # Expected: [[2,2,2],[2,2,2],[2,2,2]] 