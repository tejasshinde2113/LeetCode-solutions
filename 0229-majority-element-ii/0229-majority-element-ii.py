class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dct=dict()
        for a in nums:
            dct[a]=1+dct.get(a,0)
        
        thres = len(nums)/3
        final = []
        for key,value in dct.items():
            if(value > thres):
                final.append(key)
        return final


        