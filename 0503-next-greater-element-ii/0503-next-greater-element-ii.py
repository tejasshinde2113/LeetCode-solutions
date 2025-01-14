class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums+nums
        ptr = len(nums)-1
        st = []
        res =[ ]
        while ptr >= 0:
            temp = nums[ptr]
            while st:
                if temp < st[-1]:
                    res.append(st[-1])
                    break
                else:
                    st.pop()
            if not st:
                res.append(-1)
            st.append(temp)
            ptr-=1
        return(res[::-1][:len(nums)//2])
        