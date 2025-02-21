class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1

        count = 0 

        def check(start, end):
            nonlocal count
            if start > end or end >= len(s):  
                return

            if s[start:end+1] == s[start:end+1][::-1]: 
                count += 1  

            check(start, end + 1)  

        for i in range(len(s)):  
            check(i, i)

        return count
