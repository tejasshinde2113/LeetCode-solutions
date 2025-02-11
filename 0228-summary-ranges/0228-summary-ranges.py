class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]

        left = 0
        p1=0
        res=[]
        p2=1
        for n in (nums[1::]):
            
            if n == nums[p2-1]+1:
                p1+=1
                p2+=1
                continue
            else:
                right = nums[p2-1]
                if nums[left] == right:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left])+'->'+str(right))
                left = p2
            p1+=1
            p2+=1
        
        if len(nums)-1 == left:
            res.append(str(nums[left]))
        else:
            res.append(str(nums[left])+'->'+str(nums[-1]))
        
        return res
        
                


        