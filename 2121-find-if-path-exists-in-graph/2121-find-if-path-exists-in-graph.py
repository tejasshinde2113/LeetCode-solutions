from collections import deque, defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(source, destination):
            visited = set()
            queue = deque([source])

            while queue:
                curr = queue.popleft()
                if curr == destination:
                    return True
                visited.add(curr)
                
                for neighbor in adj_list[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor) 
                        queue.append(neighbor)

            return False

        return bfs(source, destination)
