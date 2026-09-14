class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = max(prices)
        profit = 0
        for p in prices:
            if p <= lowest:
                lowest = p
            current = p - lowest
            if current > profit:
                profit = current
        return profit