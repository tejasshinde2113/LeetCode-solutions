class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        prev =[]
        heap =[]

        c = Counter(tasks)

        for key,val in c.items():
            heapq.heappush(heap,[-val,key])
        
        time=0
        while prev or heap:
            time+=1

            

            

            if prev and prev[0][0] == time:
                i , nval, nkey  = heapq.heappop(prev)
                heapq.heappush(heap,[nval,nkey])


            if heap:
                val, key = heapq.heappop(heap)

                val+=1
                if val !=0:
                    heapq.heappush(prev, [time + n + 1,val,key])

        

        return time

        