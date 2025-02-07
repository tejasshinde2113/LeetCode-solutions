class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo={0:0}
        for a in coins:
            memo[a] = 1
        def recur(ind):
            
            if ind in memo:
                return memo[ind]
            res = float('inf')
            for coin in coins:
                if ind - coin >=0:
                    res = min(res,recur(ind-coin)+1)
                
            memo[ind] = res
            return memo[ind]
            
        
        final = (recur(amount)) 
        if final == float('inf'):
            return -1
        else:
            return final 
        