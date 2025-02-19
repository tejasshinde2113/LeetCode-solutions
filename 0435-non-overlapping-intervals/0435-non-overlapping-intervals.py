class Solution:
    def eraseOverlapIntervals(self, val: List[List[int]]) -> int:

        val.sort()

        res=val[0][1]
        cnt=0
        for i in range(1,len(val)):
            if val[i][0] <res:
                res = min(res,val[i][1])
                cnt+=1
            else:
                res = val[i][1]
        return cnt


        