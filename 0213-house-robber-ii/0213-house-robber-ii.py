class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def helper(house):

            first =0
            sec = 0
            res =0
            for money in house:
                res = max(first+money,sec)
                
                first = sec
                sec = res
            
            return res


        return max(helper(nums[:len(nums)-1]),helper(nums[1:]))