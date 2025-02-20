class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        s = []

        def create(ind,arr,r):

            if len((arr))== len(nums):
                s.append(arr[:])
                return
            for i in range(0,len(r)):
                create(i,arr+[r[i]],r[:i]+r[i+1:])


        create(0,[],nums)
        return (s)
        