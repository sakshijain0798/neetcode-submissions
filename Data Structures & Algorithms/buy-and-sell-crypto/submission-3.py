class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            if i != len(prices)-1:
                max_future= max(prices[i+1:])

                profit= max_future- prices[i]
                if profit>max_profit:
                    max_profit= profit
        return max_profit