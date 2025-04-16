from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        
        minlow = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            minlow = min(minlow, prices[i])
            profit = max(profit, prices[i] - minlow)
            
        return profit
    
    # Alternative implementation - more explicit
    def maxProfit_alt(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
            
        max_profit = 0
        min_price = prices[0]
        
        for price in prices[1:]:
            # Update min_price if current price is lower
            min_price = min(min_price, price)
            
            # Update max_profit if selling at current price would yield higher profit
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
            
        return max_profit

# Test cases
def test_max_profit():
    solution = Solution()
    
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Test Case 1: prices = {prices1}")
    print(f"Output: {solution.maxProfit(prices1)}")
    print(f"Output (alternative): {solution.maxProfit_alt(prices1)}")
    print(f"Expected: 5 (Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5)")
    print()
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Test Case 2: prices = {prices2}")
    print(f"Output: {solution.maxProfit(prices2)}")
    print(f"Output (alternative): {solution.maxProfit_alt(prices2)}")
    print(f"Expected: 0 (No transactions are done)")
    print()
    
    # Test case 3
    prices3 = []
    print(f"Test Case 3: prices = {prices3}")
    print(f"Output: {solution.maxProfit(prices3)}")
    print(f"Output (alternative): {solution.maxProfit_alt(prices3)}")
    print(f"Expected: 0 (Empty price list)")
    print()
    
    # Test case 4
    prices4 = [2, 4, 1, 7]
    print(f"Test Case 4: prices = {prices4}")
    print(f"Output: {solution.maxProfit(prices4)}")
    print(f"Output (alternative): {solution.maxProfit_alt(prices4)}")
    print(f"Expected: 6 (Buy on day 3 (price = 1) and sell on day 4 (price = 7), profit = 7-1 = 6)")
    print()
    
    # Test case 5
    prices5 = [3, 3, 3, 3]
    print(f"Test Case 5: prices = {prices5}")
    print(f"Output: {solution.maxProfit(prices5)}")
    print(f"Output (alternative): {solution.maxProfit_alt(prices5)}")
    print(f"Expected: 0 (All prices are the same)")

if __name__ == "__main__":
    test_max_profit() 