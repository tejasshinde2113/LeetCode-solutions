class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo=[0]*(amount+1)
        coins.sort()
        


        for i in range(1,amount+1):
            minVal = 999998
            for coin in coins:
                reminder = i-coin
                if reminder >=0:
                    minVal = min(minVal,memo[reminder])
                else:
                    break
            memo[i] = minVal+1
    

        if memo[amount] == 999999:
            return -1
        else:
            return memo[amount]
        