class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for a,b in points:
            heapq.heappush(heap,((a**2+b**2),[a,b]))
        res =[]
        mini = 10**6
        ss  =  heap[0][0]
        print(heap,ss)
        while k>0:
            k-=1
            
            val,arr = (heapq.heappop(heap))
              
            res.append(arr)
        return res            
        
       
        