class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dct={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res = []

        def helper(cnt, comb):
            if cnt==len(digits):
                res.append(comb)
                return
            
            for j in dct[digits[cnt]]:
                helper(cnt+1,comb+j)
        helper(0,'')
        return res if res !=[''] else []