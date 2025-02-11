class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [(-a,i) for i,a in enumerate(score)]
        heapq.heapify(score)

        res =['']*len(score)
        cnt =1
        while score:

            val,ind = heapq.heappop(score)
            if cnt==1:
                res[ind] = 'Gold Medal'
            elif cnt == 2:
                res[ind] = 'Silver Medal'
            elif cnt == 3:
                res[ind] = 'Bronze Medal'
            else:
                res[ind] = str(cnt)
            cnt+=1
        return res




        



        