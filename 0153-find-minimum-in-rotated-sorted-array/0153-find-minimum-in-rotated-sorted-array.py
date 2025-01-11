class Solution:
    def findMin(self, nums: List[int]) -> int:
        start =0
        end = len(nums)-1
        res = nums[start]
        if(nums[start]<nums[end]):
            return nums[start]
        while start<=end:
            mid = start + (end - start)//2

            if res > nums[mid]:
                res = nums[mid]

                if nums[mid] < nums[mid-1]:
                    break
                else:
                    end = mid-1
                    continue
            
            if nums[start] <= nums[mid]:
                res = min(res, nums[start])
                start = mid+1
            else:
                end = mid-1
        return res
        
            
            


           

            
        