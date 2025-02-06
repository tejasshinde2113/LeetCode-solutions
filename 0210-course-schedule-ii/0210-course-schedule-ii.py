class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = [[] for a in range(numCourses)]

        for a in prerequisites:
            adj[a[0]].append(a[1])
    

        pre = [0 for a in range(numCourses)]

        for i,a in enumerate(adj):
            for val in a:
                pre[val]+=1
        
        zero=deque([])

        for i,a in enumerate(pre):

            if a==0:
                zero.append(i)
        
        res =[]

        

        while zero:

            temp = zero.popleft()
            res.append(temp)

            for val in adj[temp]:
                pre[val]-=1
                if pre[val]==0:
                    zero.append(val)
        
        print(pre)
        return res[::-1] if  sum(pre) ==0 else []


        