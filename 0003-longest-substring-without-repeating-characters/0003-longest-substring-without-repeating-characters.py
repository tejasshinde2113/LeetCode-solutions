class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dct ={}
        p1=0
        res = 0
        for p2,val in enumerate(s):
            dct[val] = 1+ dct.get(val,0)

            if dct[val] == 1:
                res = max(res,p2-p1+1)
            
            elif dct[val] == 2:
                while dct[val] !=1:
                    dct[s[p1]] -=1
                    p1+=1
        return res



        