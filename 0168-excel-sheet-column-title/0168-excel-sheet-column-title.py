class Solution:
    def convertToTitle(self, c: int) -> str:
        res =[]
        while c>0:
            c-=1
            val = chr(c%26+ 65)
            res.append(val)
            c = c//26
        
        return ''.join(res[::-1])
