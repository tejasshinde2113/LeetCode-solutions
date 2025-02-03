class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()

        first = strs[0]
        last = strs[-1]

        res = []

        i =0
        while i < len(first) and i <len(last):
            if first[i] != last[i]:
                break
            res.append(first[i])
            i+=1
        
        return ''.join(res)
        