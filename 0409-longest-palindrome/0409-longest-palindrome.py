class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = defaultdict(int)
        for i in s:
            k = i
            c[k]+=1
        
        odd = 0
        res =0
   
        for val in c.values():
            if val%2 ==0:
                res+=val
            elif val%2:
                res+= val-1
                odd =1
        
        return res+odd