class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        for i in range(1,len(prices)):
            sell = prices[i]
            news = prices[0:i]
            buy = min(news)
            p = sell-buy
            maxp = max(maxp,p)
        if maxp<0:
            return 0
        return maxp