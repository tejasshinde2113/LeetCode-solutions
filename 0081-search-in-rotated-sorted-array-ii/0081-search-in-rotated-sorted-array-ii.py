class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l= 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                return True
            
            if nums[l] == nums[mid]:
                l+=1
                continue
            if nums[mid] == nums[r]:
                r-=1
                continue
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r -=1
                else:
                    l+=1
            else:
                if nums[mid] < target <=nums[r]:
                    l+=1
                else:
                    r-=1
        return False
        