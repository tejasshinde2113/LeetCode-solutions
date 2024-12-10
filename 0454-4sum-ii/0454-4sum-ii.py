class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        s= dict()
        for a in nums3:
            for b in nums4:
                s[a+b] = 1+ s.get(a+b,0)
        cnt=0
        for a in nums1:
            for b in nums2:
                v = a+b
                if -v in s:
                    cnt+=s[-v]
        return cnt

        