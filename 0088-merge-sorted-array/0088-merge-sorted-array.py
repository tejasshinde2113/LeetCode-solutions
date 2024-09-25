class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if(m==0):
            p1=0
            for a in nums2:
                nums1.insert(p1,a)
                nums1.pop()
                p1+=1

        elif(n==0):
            pass
        else:
            print('hi')
            p2=p1=0
            while p1<len(nums1) and  p2<n:
                if( nums2[p2]<=nums1[p1]):
                    nums1.insert(p1,nums2[p2])
                    nums1.pop()
                    p2+=1

                p1+=1
            p1=m+p2  
            while p2<n:
                nums1.insert(p1,nums2[p2])
                nums1.pop()
                p1+=1
                p2+=1


