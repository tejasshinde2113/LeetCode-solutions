class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap =[]
        for trip in trips:
            heapq.heappush(heap,(trip[1],1,trip[0]))
            heapq.heappush(heap,(trip[2],-1,trip[0]))
        
        cap = 0
        while heap:
            position, action, people = heap[0]

            if action==1:
                cap+=people
            else:
                cap-=people
            if cap > capacity:
                return False
            heapq.heappop(heap)
        return True

        