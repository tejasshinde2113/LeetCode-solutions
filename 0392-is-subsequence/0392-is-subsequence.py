class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s1=0
        t1=0

        for a in t:
            if a==s[s1]:
                s1+=1
            
            if s1== len(s):
                return True
        return False