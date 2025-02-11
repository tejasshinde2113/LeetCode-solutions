class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        peak = -1

        n = len(nums)-1
        while n>0:
            if nums[n] > nums[n-1]:
                peak = n
                break
            n-=1
        if peak == -1:
            l = 0
            r = len(nums) -1

            while l<r:
                nums[l],nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            return 

        
        ind = peak

        for i in range(peak,len(nums)):
            if nums[i]> nums[peak - 1] and nums[i]<nums[ind]:
                ind = i
        
        nums[peak-1],nums[ind] = nums[ind],nums[peak-1]

        nums[peak:] = sorted(nums[peak:])
        return


