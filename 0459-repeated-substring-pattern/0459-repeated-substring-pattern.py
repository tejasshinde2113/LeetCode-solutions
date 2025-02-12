class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        

        s2=s+s
        return s in s2[1:len(s2)-1]