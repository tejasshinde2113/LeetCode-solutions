class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1=0
        p2=1
        maxval = 0

        for i in range(1,len(prices)):
            if prices[i]> prices[i-1]:
                maxval+= (prices[i]-prices[i-1])
        return maxval