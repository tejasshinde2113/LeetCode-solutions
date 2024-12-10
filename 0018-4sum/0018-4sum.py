from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        quad = []
        nums.sort()

        def recur(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    recur(k-1,i+1,target-nums[i])
                    quad.pop()
                return
        
            p1,p2 = start,len(nums)-1  
            while p1<p2:
                if nums[p1]+nums[p2]<target:
                    p1+=1
                elif(nums[p1]+nums[p2]>target):
                    p2-=1
                else:
                    res.append(quad + [nums[p1],nums[p2]])
                    p1+=1
                    
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    
        recur(4,0,target)

        return res

       