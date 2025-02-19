class Solution:
    def findMinPath(self, triangle: list[list[int]]) -> tuple[int, list[int]]:
        """
        求数字三角形中从上到下的最小路径和以及对应路径。
        输入:
            triangle: 数字三角形，为一个二维列表，每个子列表代表一行。
        返回:
            元组 (min_sum, path)
              min_sum: 最小路径和
              path: 对应的路径（从顶到底每行选出的数字）
        """
        if not triangle:
            return 0, []
        n = len(triangle)
        # 初始化 dp 数组和 next_index 数组，dp[i][j] 表示从 (i,j) 到底部的最小路径和，
        # next_index[i][j] 用来记录在 (i,j) 处选择了下一行哪个位置。
        dp = [row[:] for row in triangle]  # 深拷贝 triangle
        next_index = [[-1] * len(row) for row in triangle]
        
        # 底层行：dp[n-1][j] 就是 triangle[n-1][j]，没有后续选择
        for j in range(len(triangle[n-1])):
            dp[n-1][j] = triangle[n-1][j]
            next_index[n-1][j] = -1
            
        # 自底向上计算 dp 值
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                # 比较两条可能的路径：左下 (i+1, j) 和右下 (i+1, j+1)
                if dp[i+1][j] <= dp[i+1][j+1]:
                    dp[i][j] = triangle[i][j] + dp[i+1][j]
                    next_index[i][j] = j
                else:
                    dp[i][j] = triangle[i][j] + dp[i+1][j+1]
                    next_index[i][j] = j + 1
        
        # 根据 next_index 重构从顶到底的路径
        path = []
        j = 0
        for i in range(n):
            path.append(triangle[i][j])
            if i < n - 1:
                j = next_index[i][j]
        return dp[0][0], path


# 测试代码
def test_triangle():
    sol = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    min_sum, path = sol.findMinPath(triangle)
    assert min_sum == 11, f"Expected 11, got {min_sum}"
    assert path == [2, 3, 5, 1], f"Expected [2, 3, 5, 1], got {path}"
    print("所有测试用例通过！")
    
if __name__ == "__main__":
    test_triangle() 