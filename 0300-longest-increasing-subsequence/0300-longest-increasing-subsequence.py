class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    memo[i] = max(memo[i],1+memo[j])
        
        return(max(memo))