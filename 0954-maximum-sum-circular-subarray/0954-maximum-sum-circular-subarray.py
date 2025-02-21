class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        

        minsum =min(nums)
        maxsum = nums[0]
        totalsum = 0

        currmax =0
        currmin = 0
        for i in nums:
            if currmax < 0:
                currmax =0
            currmax+=i
            maxsum = max(maxsum,currmax)

            currmin +=i
            minsum = min(currmin,minsum)
            if currmin > 0:
                currmin =0
            


            totalsum +=i
        

        if maxsum <0:
            return maxsum

        return max(maxsum, totalsum-minsum)
