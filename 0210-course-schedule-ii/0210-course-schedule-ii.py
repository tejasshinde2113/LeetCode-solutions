class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = [[] for a in range(numCourses)]

        for a in prerequisites:
            adj[a[0]].append(a[1])
    

        prereq = [0 for a in range(numCourses)]

        for i,a in enumerate(adj):
            for val in a:
                prereq[val]+=1

        zero=[]
        for a in range(len(adj)):
            if prereq[a] ==0:
                zero.append(a)

        if not zero:
            return []
        
        res =[]
        
       
        while zero:
            
            temp = zero[0]
            del zero[0]
            res.append(temp)

            for a in adj[temp]:
                prereq[a]-=1
                if prereq[a] ==0:
                    zero.append(a)
        
                
        return res[::-1] if sum(prereq)==0 else []
        