class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap =[]
        

        for i in range(1,len(heights)):
            diff =heights[i] - heights[i-1]
            print(bricks,ladders,i,diff)
            if diff > 0:
                if bricks >=diff:
                    bricks-=diff
                    heapq.heappush(heap,-diff)
                
                elif ladders > 0:
                    ladders-=1
                    if heap and -heap[0] > diff:  
                        bricks += -heapq.heappop(heap)  
                        bricks -= diff 
                        heapq.heappush(heap, -diff) 
                    
                else:
                    return i-1
          
        
        return len(heights)-1
                
