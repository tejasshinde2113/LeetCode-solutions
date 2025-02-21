class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        dct= Counter(s)

        for i in t:
            if i not in dct or dct[i]<1:
                return i
            dct[i]-=1
