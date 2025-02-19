class Solution:
    def insert(self, val: List[List[int]], new: List[int]) -> List[List[int]]:
        
        
        
        
        res = []
        f= True

        for start,end in val:

            if new[1] < start and f:
                res.append(new)
                res.append([start,end])
                f= False
            elif new[0] > end or new[1] < start:
                res.append([start,end])
            else:
                maxval = max(end, new[1])
                minval = min(start,new[0])
                new = [minval,maxval]
        if f:
            res.append(new)
        return res