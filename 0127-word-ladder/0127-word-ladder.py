class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        dct = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                patt = word[:i]+'*'+word[i+1:]

                dct[patt].append(word)
        
        
        visit=set()
        q = deque([beginWord])
        visit.add(beginWord)
        res =1

        while q:
            for a in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    patt = word[:i]+'*'+word[i+1:]

                    for lst in dct[patt]:
                        if lst not in visit:
                            q.append(lst)
                            visit.add(lst)
            res+=1

        return 0