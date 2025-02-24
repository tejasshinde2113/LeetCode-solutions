class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        res = []
        for i in range(numRows):
            jump = (numRows-1)*2
            for j in range(i,len(s),jump):

                res.append(s[j])
                
                if i > 0 and i < numRows-1 and j+jump - 2*i < len(s):
                    res.append(s[j+jump - 2*i])
        
        return ''.join(res)
        