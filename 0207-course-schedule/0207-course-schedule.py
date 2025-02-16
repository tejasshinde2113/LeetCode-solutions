class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]

        for course,pre in prerequisites:
            adj[course].append(pre)

        visit = [0 for i in range(numCourses)]
        path = [0 for i in range(numCourses)]


        def dfs(course):
            visit[course]=1

            path[course]=1

            for pre in adj[course]:
                if path[pre]==1:
                    return True
                else:
                    if dfs(pre):
                        return True
            path[course]=0
            return False

        for i in range(numCourses):
            if adj[i] and visit[i] ==0:
                visit[i] = 1
                if dfs(i):
                    return False
        return True