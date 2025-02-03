class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        res_dict = defaultdict(list)
        
        for word in strs:
            res_dict[str(sorted(word))].append(word) 

        return list(res_dict.values())

        # dct = defaultdict(list)


        # for val in strs:
        #     count = [0]*26

        #     for cha in val:
        #         count[ord(cha) - ord('a')] +=1
            
        #     dct[tuple(count)].append(val)
        # return list(dct.values())
        