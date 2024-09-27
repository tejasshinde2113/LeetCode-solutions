class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinctNums = set(nums)
        f=0
        if(len(distinctNums)<3):
            f=1

        distinctNums = sorted(list(distinctNums),reverse=True)
        return distinctNums[0] if f==1 else distinctNums[2]


        