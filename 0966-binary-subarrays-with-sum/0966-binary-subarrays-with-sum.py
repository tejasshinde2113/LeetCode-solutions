class Solution:

    def cal(self,goal,nums):
        p1=0
        cnt=0
        final = 0
        for p2 in range(len(nums)):
            cnt+=nums[p2]
            while(p1<=p2 and cnt>goal):
                cnt -= nums[p1]
                p1+=1
            final +=(p2-p1+1)
        print(final)
        return final
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        return self.cal(goal,nums) - self.cal(goal-1,nums)


        