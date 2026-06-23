class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1 
        maxP = 0 
        for i in range(1,len(prices)):
            if prices[l] < prices[i]:
                profit = prices[i] - prices[l]
                maxP = max(profit, maxP)
            else:
                l=i
        return maxP
    


