class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def dfs(start,cnt):
            if start < 0 or start >= len(arr) or cnt > len(arr):
                return False
            if arr[start]==0:
                return True
            return dfs(start+arr[start],cnt+1) or  dfs(start-arr[start],cnt+1)


        return dfs(start,0)
        