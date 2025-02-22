class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        res=defaultdict(list)

        for i in strs:
            arr = [0]*(26)

            for ch in i:
                ind  = ord(ch)-ord('a')
                arr[ind]+=1
            
            res[tuple(arr)].append(i)
        
        final = [val for val in res.values()]
        return final
