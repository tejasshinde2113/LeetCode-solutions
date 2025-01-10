class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ma = {}

        for a in words2:
            temp ={}
            for b in a:
                temp[b] = 1+ temp.get(b,0)
            
            for aa in temp:
                if aa not in ma or temp[aa] > ma[aa]:
                    ma[aa]= temp[aa]
        final =[]
        for a in words1:
            temp ={}
            f = True
            for b in a:
                temp[b] = 1+ temp.get(b,0)
            for aa in ma:
                
                if aa not in temp or temp[aa] < ma[aa]:
                    f = False
            if f:
                final.append(a)
        return final





        