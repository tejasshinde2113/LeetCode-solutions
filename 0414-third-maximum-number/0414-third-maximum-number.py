class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m,m2,m3=None,None,None

        s= set(nums)

        for a in s:

            if m==None or a>m:
                m3=m2
                m2=m
                m = a
            elif m2==None or a>m2:
                m3=m2
                m2=a
            elif m3==None or a>=m3:
                m3=a
        return m3 if m3 is not None else m
    
        