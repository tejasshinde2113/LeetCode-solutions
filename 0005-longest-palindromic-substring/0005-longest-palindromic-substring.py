class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans =  ''


        def check(l,r):
            nonlocal ans
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > len(ans):
                    ans = s[l:r+1]
                l-=1
                r+=1
        for i in range(len(s)):

            check(i,i)
            check(i,i+1)
        return ans
            
            
