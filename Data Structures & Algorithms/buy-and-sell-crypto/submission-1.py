class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = prices[0]
        Max_Profit = 0
        max_now = 0 
        for i in range(1, len(prices)):
            if prices[i-1] < min_left:
                min_left = prices[i-1]
            max_now = prices[i] - min_left    
            if max_now > Max_Profit:
                Max_Profit  = max_now
        if Max_Profit > 0:
            return Max_Profit
        else:
            return 0
