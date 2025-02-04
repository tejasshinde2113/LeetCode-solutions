class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        right = Counter(s)
        left = set()
        res = set()

        for a in s:
            right[a]-=1

            for x in 'abcdefghijklmnopqrstuvwxyz':
                if x in left and right[x] > 0:
                    res.add(x+a+x)
            
            left.add(a)
        return len(res)