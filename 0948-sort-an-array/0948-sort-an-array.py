class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def combine(l,r,mid):

            temp1 = nums[l:mid+1] +[float('inf')]
            temp2 = nums[mid+1:r+1] +[float('inf')]
            res =[]
            p1=0
            p2=0
            for i in range(l,r+1):
                if temp1[p1]>temp2[p2]:
                    res.append(temp2[p2])
                    p2+=1
                else:
                    res.append(temp1[p1])
                    p1+=1
            for i in range(l, r + 1):
                nums[i] = res[i - l]
            
            return nums


        def mergesort(l,r):
            if l<r:
                m = l+(r-l)//2
                mergesort(l,m)
                mergesort(m+1,r)

                return combine(l,r,m)
        
        (mergesort(0,len(nums)-1))
        return nums