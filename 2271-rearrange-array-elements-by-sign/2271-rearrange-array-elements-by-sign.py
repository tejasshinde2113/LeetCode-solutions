class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        ans=[0]*len(nums)

        p=0
        n=1

        for i in nums:
            if i>0:
                ans[p]=i
                p+=2
            else:
                ans[n]=i
                n+=2
        return ans
