class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maximum=1
        minimum = 1
        res = nums[0]
        for num in nums:

            temp = maximum
            maximum = max(maximum*num, minimum*num, num)
            minimum = min(temp*num, minimum*num, num)

            res = max(res,maximum)



        return res
