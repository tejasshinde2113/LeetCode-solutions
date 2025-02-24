class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)<2:
            return 0

        def helper(p,direction):
            opens =0
            closes =0
            res =0
            for ch in p:
                if ch =='(':
                    opens+=1
                else:
                    closes+=1
                
                if opens==closes:
                    res = max(res,opens+closes)
                if not direction:
                    if opens < closes:
                        opens=0
                        closes=0
                else:
                    if opens > closes:
                        opens=0
                        closes=0
            print(res,direction)
            return res

        
        return max(helper(s,0),helper(s[::-1],1))