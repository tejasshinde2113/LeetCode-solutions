class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        visit =set()

        q=deque([s])

        while q:
            temp = q.popleft()
            if temp in visit:
                continue
            if temp == '':
                return True
            visit.add(temp)
            

            for val in wordDict:
                if len(temp)>= len(val) and val == temp[:len(val)]:
                    q.append(temp[len(val):])

        return False