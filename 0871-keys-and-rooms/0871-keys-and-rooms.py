class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def bfs(dct):

            visited = set()
            queue = [0]

            while (queue != []):
                curr = queue[-1]
                del queue[-1]

                if(curr not in visited):
                    visited.add(curr)

                    if(curr in dct):
                        for neigh in dct[curr]:
                            if(neigh not in visited):
                                queue.append(neigh)
            return (visited)

        dct = dict()
        for i,a in enumerate(rooms):
            dct[i]=a
        
        visited = bfs(dct)

        final = []
        for a in rooms:
            final.extend(a)
        final = set(final)

        

        if 0 not in final:
            final.add(0)

        print(visited)
        print(final)
        print(len(rooms))

        return len(visited) == len(final) == len(rooms)
        