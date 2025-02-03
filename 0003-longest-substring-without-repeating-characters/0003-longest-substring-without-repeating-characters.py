class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dct =set()
        p1=0
        res = 0
        for p2,val in enumerate(s):
            while  val in dct:
                    dct.remove(s[p1])
                    p1+=1
            dct.add(val)

            res = max(res,p2-p1+1)
            
            
        return res



        