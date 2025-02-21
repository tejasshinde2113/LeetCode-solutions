class Solution:
    def romanToInt(self, s: str) -> int:
        dct ={
            'O':0,
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        res = 0
        for i in range(len(s)):
            if i+1 < len(s):
                if dct[s[i]] <dct[s[i+1]]:
                    res -= dct[s[i]]
                else:
                    res+= dct[s[i]]
            else:
                res+=dct[s[i]]
        
        return res