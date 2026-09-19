class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        maxp=0
        for i in range(1,len(prices)):
            p = prices[i]-buy
            maxp = max(maxp,p)
            buy = min(buy,prices[i])
        return maxp