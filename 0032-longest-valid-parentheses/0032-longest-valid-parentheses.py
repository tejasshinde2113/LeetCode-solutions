class Solution:
    def longestValidParentheses(self, s: str) -> int:

        res = 0
        l=0
        r=0

        for ch in s:
            if ch == '(':
                l+=1
            else:
                r+=1
            if r==l:
                res = max(res,l*2)
            if r>l:
                res = max(res,l*2)
                l=0
                r=0

        l=0
        r=0

        for ch in s[::-1]:
            if ch == '(':
                l+=1
            else:
                r+=1
            if r==l:
                res = max(res,l+r)
            if r<l:
                res = max(res,r*2)
                l=0
                r=0
        
        

        return res
        