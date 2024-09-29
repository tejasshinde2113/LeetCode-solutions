class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        final =[-1,-1]

        start =0
        end = len(nums)-1

        while start<=end:
            mid = start + (end-start)//2
            if(nums[mid] == target):
                final[0] = mid
                end = mid -1
                continue
            if(nums[mid]<target):
                start=mid+1
            else:
                end = mid -1

        start =0
        end = len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if(nums[mid] == target):
                final[1] = mid
                start = mid+1
                continue
            if(nums[mid]<target):
                start=mid+1
            else:
                end = mid -1
        return final
        