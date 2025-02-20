class Solution:

    def compare(self, left,right):
        
        return left+right > right+left

    def combine(self,nums,l,r,m):
        left = nums[l:m+1] 
        right = nums[m+1:r+1] 
        p1 =0
        p2=0
        res = []

        while p1 < len(left) and p2 < len(right):
            if self.compare(left[p1],right[p2]):
                res.append(left[p1])
                p1+=1
            else:
                res.append(right[p2])
                p2+=1
        
        res = res + left[p1:] +right[p2:]
        nums[l:r + 1] = res



         

    def mergesort(self,nums,l,r):
        if l<r:

            m = (l+r)//2

            self.mergesort(nums,l,m)
            self.mergesort(nums,m+1,r)

            return self.combine(nums,l,r,m)

    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(num) for num in nums ]

        res = self.mergesort( nums,0,len(nums)-1)
        
        if nums[0] == '0': 
            return '0'
        return ''.join(nums)