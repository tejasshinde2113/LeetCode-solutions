class Solution:
    def countSubstrings(self, s: str) -> int:

        cnt=0
        for i in range(len(s)):

            p1=i
            p2=i
            while p1>=0 and p2<len(s) and s[p1]==s[p2]:
                cnt+=1
                p1-=1
                p2+=1
            p1=i
            p2=i+1
            while p1>=0 and p2<len(s) and s[p1]==s[p2]:
                cnt+=1
                p1-=1
                p2+=1
            
        return cnt