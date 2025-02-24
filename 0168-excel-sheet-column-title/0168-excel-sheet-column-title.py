class Solution:
    def convertToTitle(self, c: int) -> str:

        res = []

        while c > 0:
            c-=1
            alpha = chr(ord('A')+ c%26)
            res.append(alpha)
            c = c//26
        
        return ''.join(res[::-1])