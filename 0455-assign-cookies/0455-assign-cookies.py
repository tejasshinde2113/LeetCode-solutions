class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g1=0
        s1=0
        cnt = 0
        while g1 < len(g) and s1 < len(s):

            if g[g1] <=s[s1]:
                cnt+=1
                g1+=1
                s1+=1
            else:
                s1+=1
        return cnt