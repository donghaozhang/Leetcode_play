class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 辅助函数：检查在 (row,col) 处填入 ch 是否合法
        def is_valid(row: int, col: int, ch: str) -> bool:
            # 检查行
            for i in range(9):
                if board[row][i] == ch:
                    return False
            # 检查列
            for i in range(9):
                if board[i][col] == ch:
                    return False
            # 检查 3x3 宫
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def backtrack() -> bool:
            # 寻找下一个空格
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        # 尝试填入 '1' ~ '9'
                        for ch in "123456789":
                            if is_valid(row, col, ch):
                                board[row][col] = ch
                                if backtrack():
                                    return True
                                # 回溯
                                board[row][col] = '.'
                        # 当前空位不能填入任何数字，返回 False
                        return False
            # 所有格子均填满，返回 True
            return True

        backtrack()


# 测试代码
def test_sudoku_solver():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    solution = Solution()
    solution.solveSudoku(board)
    
    # 打印填充后的棋盘
    for row in board:
        print(" ".join(row))

if __name__ == "__main__":
    test_sudoku_solver() 