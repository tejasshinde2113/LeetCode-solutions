class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        N = len(nums)
        end = N-1
        if N ==1:
            return nums[0]
        if(nums[-1]!=nums[-2]):
            return nums[-1]
        if(nums[0]!=nums[1]):
            return nums[0]
        while start<=end:
            mid = start + (end -start)//2
            if(nums[mid] != nums[(mid +N -1 )%N] and nums[mid]!= nums[(mid+1)%N]):
                return nums[mid]
            if(nums[mid] != nums[(mid +N -1 )%N]):
                if(((mid +N -1 )%N+1)%2 ==0):
                    start = mid +2
                else:
                    end = mid-1
            else:
                if((N- (mid+1)%N )%2 ==0):
                    end = mid -2
                else:
                    start = mid+1
        return -1
        
                