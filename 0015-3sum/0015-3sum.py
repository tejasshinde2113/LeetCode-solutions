class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for const in range(len(nums)):
            if nums[const] == nums[const-1] and const>0:
                continue
            p1 = const+1
            p2=len(nums)-1
            
            while p1<p2:
                
                s =  nums[const] + nums[p1] + nums[p2]
                
                if s == 0:
                    
                    
                    res.append([nums[const], nums[p1], nums[p2]])
                    
                    p1+=1
                    while nums[p1]== nums[p1-1] and p1<p2:
                        p1+=1
                elif s < 0:
                    p1+=1
                else:
                    p2-=1
        return (res)
            
        