class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        res =set()

        left = set()
        right = Counter(s)
        for i in s:
            right[i]-=1
            
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch in left and right[ch]>0:
                    
                    res.add(ch+i+ch)
            left.add(i)
            
        return len(res)