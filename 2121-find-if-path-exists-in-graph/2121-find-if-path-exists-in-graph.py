class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:


        def bfs(dct,source, dest):

            visited = set()
            queue = [source]

            while (queue != []):
                

                curr = queue[-1]
                del queue[-1]
                if(curr == dest):
                        return True

                if(curr not in visited):
                    visited.add(curr)

                    if(curr in dct):
                        for neigh in dct[curr]:
                            if(neigh == dest):
                                
                                return True
                            if(neigh not in visited):
                                queue.append(neigh)
            return False


        dct =dict()
        for vals in edges:
            if(vals[0] not in dct):
                dct[vals[0]] = []
            dct[vals[0]].append(vals[1])
            if(vals[1] not in dct):
                dct[vals[1]] = []
            dct[vals[1]].append(vals[0])
        
        print(dct)
        

        return bfs(dct,source,destination)
        