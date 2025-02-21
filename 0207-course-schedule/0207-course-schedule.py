class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for i in range(numCourses)]

        prereq = [0]*(numCourses)

        for course,pre in prerequisites:
            adj[pre].append(course)
            prereq[course]+=1
        

        zero=deque([i for i in range(len(prereq)) if prereq[i]==0])

        res =[]

        while zero:
            course = zero.popleft()
            res.append(course)
            for pre in adj[course]:
                prereq[pre]-=1
                if prereq[pre]==0:
                    zero.append(pre)
        
        return  True if sum(prereq)==0 else False
        