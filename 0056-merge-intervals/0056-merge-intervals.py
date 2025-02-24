class Solution:
    def merge(self, val: List[List[int]]) -> List[List[int]]:
        val.sort()
        res =[val[0]]
        for start,end in val[1:]:

            if start <= res[-1][1]:
                maxval = max(res[-1][1],end)
                minval = min(res[-1][0], start)
                res.pop()
                res.append([minval,maxval])
            
            else:
                res.append([start,end])
        
        return res
        
        