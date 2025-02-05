class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        
        ind = p.index('*')

        halfCorrect = False
        first = p[:ind]
        secind = 0
        for i in range(len(s)-len(first)+1):
            if first == s[i:i+len(first)]:
                halfCorrect = True
                secind = i+len(first)
                break
        
        if not halfCorrect:
            return False
        
        

        

        sec = p[ind+1:]

        if not sec:
            return True
        

        if not first:
            secind = 0
        
        return True if sec in s[secind:] else False
        




        