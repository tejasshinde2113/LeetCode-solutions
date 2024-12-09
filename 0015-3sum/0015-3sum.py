class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,a in enumerate(nums):
            if a == nums[i-1] and i>0:
                continue
            
            p1=i+1
            p2 = len(nums)-1
            while p1<p2:
                if a + nums[p1]+nums[p2] == 0:
                    res.append([a,nums[p1],nums[p2]])
                    p1+=1
                    while nums[p1]==nums[p1-1] and p1<p2:
                        p1+=1
                elif a + nums[p1]+nums[p2] > 0:
                    p2-=1
                else:
                    p1+=1
        return res
                    
        