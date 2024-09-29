class Solution:
    def findMin(self, nums: List[int]) -> int:
        start =0
        end = len(nums)-1
        N = len(nums)
        if(nums[start]<=nums[end]):
            return nums[start]
        while start<=end:
            mid = start + (end - start)//2
            prev = (mid+N-1)%N
            nxt = (mid+1)%N
            if(nums[mid]<nums[prev] and nums[mid]<nums[nxt]):
                return nums[mid]
            if(nums[mid]>=nums[0]):
                start = mid+1
            else:
                end = mid-1

            
        