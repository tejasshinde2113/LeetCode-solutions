class Solution:
    def merge(self, val: List[List[int]]) -> List[List[int]]:
        val.sort()

        res = [val[0]]

        for i in range(1,len(val)):
            if val[i][0] <= res[-1][1]:
                
                sec = max(res[-1][1], val[i][1])
                first = min (res[-1][0], val[i][0])
                res.pop()
                res.append([first, sec])
            else:
                res.append(val[i])
        
        return res
