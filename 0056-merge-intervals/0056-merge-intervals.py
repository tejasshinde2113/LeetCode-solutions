class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a=0
        intervals.sort()
        while a < len(intervals)-1:
            if(intervals[a][-1] >= intervals[a+1][0] and intervals[a+1][0] > intervals[a][0]):
                intervals[a+1] = [intervals[a][0],max(intervals[a+1][-1],intervals[a][-1])]
                del intervals[a]
            elif(intervals[a][-1] >= intervals[a+1][0] and intervals[a+1][0] <= intervals[a][0]):
                del intervals[a]
            else:
                a+=1
        return intervals


        