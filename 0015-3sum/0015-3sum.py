class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,a in enumerate(nums[:len(nums)-2]):
            if i >0  and nums[i] == nums[i-1]:
                continue
            
            p1 = i+1
            p2 = len(nums)-1

            while p1 < p2:
                temp = nums[p1]+nums[p2]+nums[i]
                if temp == 0:
                    res.append([nums[p1],nums[p2],nums[i]])
                    p1+=1
                    while p1 < len(nums) and nums[p1] == nums[p1-1]:
                        p1+=1
                    while p2 > 0 and nums[p2] == nums[p2-1]:
                        p2-=1
                elif temp < 0:
                    p1+=1
                else:
                    p2-=1
        return res

