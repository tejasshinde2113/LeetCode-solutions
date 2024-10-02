class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1 = len(nums1)-1
        n2 = 0
        while n1>=0 and n2<len(nums2):
            if(nums1[n1]> nums2[n2]):
                nums1[n1],nums2[n2] = nums2[n2],nums1[n1]
                n1-=1
            n2+=1
        tot = nums1 + nums2
        tot.sort()
        mid = (len(tot)-1)//2
        if(len(tot)%2 ==0):
            return float((tot[mid]+tot[mid+1])/2)
        else:
            return float(tot[mid])
        

        