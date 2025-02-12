class Solution:
    def convertToTitle(self, c: int) -> str:

        res =[]
        while c> 0:
            c -=1
            alpha = chr(c%26 + ord('A'))
            res.append(alpha)
            c = c//26
         
        return ''.join(res[::-1])
