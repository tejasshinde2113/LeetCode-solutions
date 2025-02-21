class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows ==1:
            return s

        res = []

        for row in range(numRows):
            jump = (numRows-1)*2

            for i in range(row,len(s),jump):
                res.append(s[i])

                if row >0 and row < numRows-1 and i+jump - 2*row < len(s):
                    res.append(s[i+jump - 2*row])

        return ''.join(res)