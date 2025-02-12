class Solution:
    def lengthOfLastWord(self, s: str) -> int:


        res = []
        start =0
        p2=0
        for i in s:
            if i==' ':
                if start:
                    res.append(start)
                    start=0
            elif i:
                start+=1

            p2+=1
        if start:
            return start
        return res[-1]
            
            
        