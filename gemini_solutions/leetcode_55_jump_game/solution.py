# Test Suite
class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.canJump([2, 3, 1, 1, 4]), "Test Case 1 Failed: Example 1")

    def test_example2(self):
        self.assertFalse(self.solution.canJump([3, 2, 1, 0, 4]), "Test Case 2 Failed: Example 2")

    def test_single_zero(self):
        # Start and end at index 0, which is reachable.
        self.assertTrue(self.solution.canJump([0]), "Test Case 3 Failed: Single Zero") 

    def test_single_non_zero(self):
        # Start and end at index 0, which is reachable.
        self.assertTrue(self.solution.canJump([1]), "Test Case 4 Failed: Single Non-Zero") 

    def test_stuck_at_start(self):
        # From index 0, max jump is 0. Cannot move. Last index (1) is unreachable.
        self.assertFalse(self.solution.canJump([0, 1]), "Test Case 5 Failed: Stuck at Start")

    def test_simple_jump_to_end(self):
        # From index 0, jump 1 step to index 1 (last index).
        self.assertTrue(self.solution.canJump([1, 0]), "Test Case 6 Failed: Simple Jump to End")

    def test_jump_over_zero(self):
        # From index 0, can jump 2 steps to index 2 (last index).
        self.assertTrue(self.solution.canJump([2, 0, 0]), "Test Case 7 Failed: Jump Over Zero")

    def test_all_ones(self):
        # Can always jump 1 step forward, eventually reaching the end.
        self.assertTrue(self.solution.canJump([1, 1, 1, 1]), "Test Case 8 Failed: All Ones")

    def test_blocked_by_zero(self):
        # 0 -> 1 -> 2. At index 2, nums[2]=0. Cannot jump further. Last index (3) unreachable.
        self.assertFalse(self.solution.canJump([1, 1, 0, 1]), "Test Case 9 Failed: Blocked by Zero")
        
    def test_long_jump_sufficient(self):
        # From index 0, can jump up to 5 steps. Can directly reach index 5 (last index).
        self.assertTrue(self.solution.canJump([5, 0, 0, 0, 0, 0]), "Test Case 10 Failed: Long Jump Sufficient")

    def test_cannot_reach_end_complex(self):
        # 0 -> 1. At index 1, nums[1]=0. Stuck. Cannot reach index 2 or 3.
        self.assertFalse(self.solution.canJump([1, 0, 1, 0]), "Test Case 11 Failed: Cannot Reach End Complex")

    def test_large_input_true(self):
        # Array of 10000 ones, should be able to reach the end.
        self.assertTrue(self.solution.canJump([1] * 10000), "Test Case 12 Failed: Large Input True")

    def test_large_input_true_with_zero(self):
        # Array of 9999 ones followed by zero. Can reach the last index.
        self.assertTrue(self.solution.canJump([1] * 9999 + [0]), "Test Case 13 Failed: Large Input True w/ Zero")

    def test_large_input_false(self):
        # Blocked by a zero partway through.
        nums = [1] * 5000 + [0] + [1] * 4999
        self.assertFalse(self.solution.canJump(nums), "Test Case 14 Failed: Large Input False")

# To run the tests (e.g., save as 'test_jump_game.py' and run 'python -m unittest test_jump_game.py')
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
