class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        right = Counter(s)
        left = set()
        res = set()

        words = set(list(s))
        for a in s:
            right[a]-=1

            for x in left:
                if right[x] > 0:
                    res.add(x+a+x)
            
            left.add(a)
        return len(res)