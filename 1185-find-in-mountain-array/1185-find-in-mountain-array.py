# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = mountainArr.length()
        start = 1 
        end = l-2
        peak = None
        while start<=end:
            mid = ((start)+(end))//2
            
            midVal = mountainArr.get(mid)
            backVal = mountainArr.get(mid-1)
            frontVal = mountainArr.get(mid+1)
          
            if backVal < midVal > frontVal:
                peak = mid
                break
                
            if backVal < midVal < frontVal:
                start = mid+1
            else:
                end = mid-1
           
        
        res = l

        start = 0
        end = peak

        while start <= end:
            mid = ((start)+(end))//2

            midVal = mountainArr.get(mid)
            if midVal == target:
                res = min(res,mid)
            
            if target <= midVal:
                end = mid-1
            else:
                start = mid+1

        start = peak
        end = l-1

        while start <= end:
            mid = ((start)+(end))//2

            midVal = mountainArr.get(mid)
            if midVal == target:
                res = min(res,mid)
            
            if target <= midVal:
                start = mid+1
                
            else:
                end = mid-1
                

        
        return res if res != l else -1
        

