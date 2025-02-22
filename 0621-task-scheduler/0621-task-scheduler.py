class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        prev =[]
        heap =[]

        c = Counter(tasks)

        for key,val in c.items():
            heapq.heappush(heap,[-val,key])
        
        cnt =0
        while prev or heap:

            for i in range(len(prev)):
                prev[i][0]-=1

            

            if prev and prev[0][0] == 0:
                i , nval, nkey  = heapq.heappop(prev)
                heapq.heappush(heap,[nval,nkey])


            if heap:
                val, key = heapq.heappop(heap)

                val+=1
                if val !=0:
                    heapq.heappush(prev, [n+1,val,key])

            cnt+=1
        

        return cnt

        