class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res=[]

        for a in range(n):
            for b in range(n):
                if a!=b and words[a] in words[b] and words[a] not in res:
                    res.append(words[a])
        
        return res

        