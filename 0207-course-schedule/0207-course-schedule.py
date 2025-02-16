class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for a in range(numCourses)]
        prereq = [0 for a in range(numCourses)]

        for course,pre in prerequisites:
            adj[course].append(pre)
            prereq[pre]+=1
        
        
        
        

        zero = deque([])

        for i,val in enumerate(prereq):
            if not val:
                zero.append(i)

        res =[]

        while zero:
            temp = zero.popleft()
            res.append(temp)

            for val in adj[temp]:
                prereq[val]-=1
                if prereq[val]==0:
                    zero.append(val)
        
        
        return True if sum(prereq) ==0 else False
