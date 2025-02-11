class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k= 0
        p1=0
        p2=len(nums)-1

        

        while p1<=p2:
            
            if nums[p1]==val:
                nums[p1],nums[p2] = nums[p2],nums[p1]
                
                p2-=1
            else:
                p1+=1
        
        return p2+1
        