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

        def back(cnt,strs):
            nonlocal res
            
            if len(strs)==len(digits):
                res.append(strs)
                return
            
            for val in dct[digits[cnt]]:
                back(cnt+1, strs+val)

        if digits:
            back(0,'')
            return res
        
        return res


        