class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dct={}
        dct2={}
        p = list(pattern)
        s = s.split(' ')
        if len(p)!= len(s):
            return False
        
        for i,val in enumerate(p):
            if val in dct:
                if dct[val] != s[i]:
                    return False
            if s[i] in dct2 and dct2[s[i]] != val:
                return False
            dct[val] = s[i]
            dct2[s[i]] = val

        return True 
        