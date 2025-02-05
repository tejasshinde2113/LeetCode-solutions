class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = 0
        ans =  ''
        for i in range(len(s)):

            l = r= i

            while l >=0 and r<len(s) and s[l]==s[r]:
                res = max(res,r-l+1)
                if len(ans)  < r-l+1:
                    ans = s[l:r+1]

                l-=1
                r+=1
            
                

            l = i
            r= i+1

            while l >=0 and r<len(s) and s[l]==s[r]:
                res = max(res,r-l+1)
                if len(ans)  < r-l+1:
                    ans = s[l:r+1]
                l-=1
                r+=1
                    
        return ans
        