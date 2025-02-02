class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1=0
        p2=1
        maxval = 0
        while p2<len(prices):
            val = prices[p2] - prices[p1]
            if(val > 0 ):
                
                maxval += val
            p2+=1
            p1=p2-1
        return maxval