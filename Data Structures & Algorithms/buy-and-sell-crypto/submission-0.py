class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, diff = prices[0], 0
        i = 0
        for i in range(0, len(prices)):
            if prices[i] <= buy:
                buy = prices[i]
            else:
                curr = prices[i] - buy
                if curr >= diff:
                    diff = curr
        return diff
        