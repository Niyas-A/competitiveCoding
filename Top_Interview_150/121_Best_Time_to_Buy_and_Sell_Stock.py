class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        sell = [0]*n
        buy = [0]*n
        sell[0] = -prices[0]
        buy[0] = prices[0]
        for i in range(1,n):
            sell[i] = max(prices[i]-buy[i-1],sell[i-1]) 
            buy[i] = min(prices[i],buy[i-1])
        print(sell)
        print(buy)
        if sell[n-1]<0:
            return 0
        else:
            return sell[n-1]