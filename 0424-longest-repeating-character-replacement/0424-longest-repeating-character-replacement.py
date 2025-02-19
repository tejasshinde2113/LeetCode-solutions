class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        dct = {}
        p1 = 0
        res =0
        for p2,i in enumerate(s):
            dct[i] = 1+dct.get(i,0)
            maxf = max(dct.values())

            
            while p2-p1+1 - maxf > k:
                dct[s[p1]]-=1
                p1+=1
            
            if p2-p1+1 - maxf <= k:
                res = max(res,p2-p1+1) 

        return res


        