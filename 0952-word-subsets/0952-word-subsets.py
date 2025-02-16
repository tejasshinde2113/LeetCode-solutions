class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count2 = defaultdict(int)

        for w in words2:
            temp = Counter(w)

            for k,val in temp.items():
                count2[k] = max(count2[k],val)
        

        res =[]
        for word in words1:
            count = Counter(word)

            isSubset = True
            for k,v in count2.items():

                if v > count.get(k,0):
                    isSubset = False
                    break
            
            if isSubset:
                res.append(word)

        return res
