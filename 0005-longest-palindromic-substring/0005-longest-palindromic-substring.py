class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans =  ''
        for i in range(len(s)):

            l = r= i

            while l >=0 and r<len(s) and s[l]==s[r]:
                if len(ans)  < r-l+1:
                    ans = s[l:r+1]

                l-=1
                r+=1
            
            l = i
            r= i+1

            while l >=0 and r<len(s) and s[l]==s[r]:
                if len(ans)  < r-l+1:
                    ans = s[l:r+1]
                l-=1
                r+=1
                    
        return ans
        