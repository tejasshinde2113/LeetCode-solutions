class Solution:
    def check(self, nums: List[int]) -> bool:

        cnt = 1
        check =0
        i= 1
        size = len(nums)
        while check <2:
            if cnt == size:
                return True
            if nums[i%size] < nums[(i-1)%size]:
                check +=1
                cnt=1
            else:
                cnt+=1
            
            i+=1
        return False


        