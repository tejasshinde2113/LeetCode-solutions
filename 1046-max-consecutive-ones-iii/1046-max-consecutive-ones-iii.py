class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero = 0
        p1=0
        temp=0
        res = 0
        for p2,n in enumerate(nums):

            zero += (not n)
            temp+=n
            if zero >k :
                temp -= nums[p1]
                if nums[p1] ==0:
                    zero-=1
                p1+=1
            res = max(res,temp+zero)
        return res
                


        