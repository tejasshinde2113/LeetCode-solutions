class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True

        p1=0

        for i in t:
            if i==s[p1]:
                p1+=1
                if p1== len(s):
                    return True
        
        return False
        