class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()


        res =[]
        arr=[]
        def helper(start, k, target):
            if k !=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    
                    arr.append(nums[i])
                    helper(i+1,k-1,target - nums[i])
                    arr.pop()
                return
            
            p1=start
            p2=len(nums)-1
            while p1<p2:
                curr = nums[p1]+nums[p2]

                if curr < target:
                    p1+=1
                elif curr > target:
                    p2-=1
                else:
                    res.append(arr+[nums[p1],nums[p2]])
                    p1+=1
                    while p1 < p2 and nums[p1]==nums[p1-1]:
                        p1+=1
                    p2-=1
        


        helper(0,4,target)
        return res
        