class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float("inf")

        for i,a in enumerate(nums):
            p1=i+1
            p2= len(nums)-1
            while p1<p2:
                s = a+nums[p1]+nums[p2]
                # print(a,nums[p1],nums[p2])
                # if a == nums[p1]==nums[p2]==1:
                #     print( abs(target - s) , abs(res-s))
                if abs(target - s) < abs(res-target):
                    res = s
                if s < target:
                    p1+=1
                elif s > target:
                    p2-=1
                else:
                    return target
        return res
