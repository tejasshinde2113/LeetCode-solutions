class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = { }
        for course in range((numCourses)):
            adj[course] = []
        for course, pre in (prerequisites):
            adj[course].append(pre)
        

        
        visit = [0 for a in range(numCourses)]
        path = [0 for a in range(numCourses)]
        st=[]
        cycle = [False]
        def dfs(i):
            if path[i] ==1:
                cycle[0] = True
            if visit[i]==1:
                return
            visit[i]=1
            
            if adj[i]:
                for pre in adj[i]:
                    path[i]=1
                    dfs(pre)
            st.append(i)

            path[i]=0
            visit[i]=1
        for i,a in (adj.items()):
            if visit[i] ==0:
                dfs(i)
                if cycle[0]:
                    return []
        return st
        
        