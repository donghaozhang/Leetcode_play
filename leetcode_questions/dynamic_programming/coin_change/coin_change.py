from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
    
    # Alternative implementation - more straightforward
    def coinChange_alt(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with amount+1 (representing infinity)
        # dp[i] represents the minimum number of coins needed to make amount i
        dp = [amount+1] * (amount+1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount] if dp[amount] <= amount else -1

# Test cases
def test_coin_change():
    solution = Solution()
    
    # Test case 1
    coins1 = [1, 2, 5]
    amount1 = 11
    print(f"Test Case 1: coins = {coins1}, amount = {amount1}")
    print(f"Output: {solution.coinChange(coins1, amount1)}")
    print(f"Output (alternative): {solution.coinChange_alt(coins1, amount1)}")
    print(f"Expected: 3 (11 = 5 + 5 + 1)")
    print()
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    print(f"Test Case 2: coins = {coins2}, amount = {amount2}")
    print(f"Output: {solution.coinChange(coins2, amount2)}")
    print(f"Output (alternative): {solution.coinChange_alt(coins2, amount2)}")
    print(f"Expected: -1")
    print()
    
    # Test case 3
    coins3 = [1]
    amount3 = 0
    print(f"Test Case 3: coins = {coins3}, amount = {amount3}")
    print(f"Output: {solution.coinChange(coins3, amount3)}")
    print(f"Output (alternative): {solution.coinChange_alt(coins3, amount3)}")
    print(f"Expected: 0")
    print()
    
    # Test case 4
    coins4 = [1, 3, 4, 5]
    amount4 = 7
    print(f"Test Case 4: coins = {coins4}, amount = {amount4}")
    print(f"Output: {solution.coinChange(coins4, amount4)}")
    print(f"Output (alternative): {solution.coinChange_alt(coins4, amount4)}")
    print(f"Expected: 2 (7 = 3 + 4)")
    print()
    
    # Test case 5
    coins5 = [2, 5, 10, 1]
    amount5 = 27
    print(f"Test Case 5: coins = {coins5}, amount = {amount5}")
    print(f"Output: {solution.coinChange(coins5, amount5)}")
    print(f"Output (alternative): {solution.coinChange_alt(coins5, amount5)}")
    print(f"Expected: 4 (27 = 10 + 10 + 5 + 2)")

if __name__ == "__main__":
    test_coin_change() 