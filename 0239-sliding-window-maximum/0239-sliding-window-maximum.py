class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p1=0
        p2=0
        st = []
        res = []
        ptr = []

        while p2<len(nums):
            st.append(nums[p2])

            while ptr and ptr[-1]<nums[p2]:
                ptr.pop()
            ptr.append(nums[p2])
            if p2-p1+1 == k:
                res.append(ptr[0])
                if ptr[0] == st[0]:
                    ptr.pop(0)
                st.pop(0)
                p1+=1
            p2+=1
        return(res)

        