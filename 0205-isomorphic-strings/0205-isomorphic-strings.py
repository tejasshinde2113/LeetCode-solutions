from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for i in range(len(s)):
            a[s[i]] = 1+ a.get(s[i],0)
            b[t[i]] = 1+ b.get(t[i],0)

            if (list(a.values()) != list(b.values())):
                return False
        return True
        