class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        cols = set()             # 记录已占用的列
        hill_diagonals = set()   # 记录 (row - col) 所在的"右上到左下"对角线
        dale_diagonals = set()   # 记录 (row + col) 所在的"左上到右下"对角线

        def backtrack(row: int):
            nonlocal count
            # 当 row == n 时，说明已经成功放置 n 个皇后
            if row == n:
                count += 1
                return
            for col in range(n):
                if col in cols or (row - col) in hill_diagonals or (row + col) in dale_diagonals:
                    continue
                # 放置皇后
                cols.add(col)
                hill_diagonals.add(row - col)
                dale_diagonals.add(row + col)
                backtrack(row + 1)
                # 回溯：撤销之前放置的皇后
                cols.remove(col)
                hill_diagonals.remove(row - col)
                dale_diagonals.remove(row + col)
        backtrack(0)
        return count


# 测试代码
def test_total_n_queens():
    sol = Solution()
    # 对于 n=4，期望解数为 2
    assert sol.totalNQueens(4) == 2, f"Expected 2, got {sol.totalNQueens(4)}"
    # 对于 n=1，期望解数为 1
    assert sol.totalNQueens(1) == 1, f"Expected 1, got {sol.totalNQueens(1)}"
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_total_n_queens() 