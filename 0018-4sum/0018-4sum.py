class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        fixed =[]
        def recur(k,start,target):

            if k != 2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i] == nums[i-1]:
                        continue
                    fixed.append(nums[i])
                    recur(k-1,i+1,target-nums[i])
                    fixed.pop()
                return
            
            p1=start
            p2 = len(nums)-1
            while p1<p2:

                currSum = sum([fixed[0],fixed[1],nums[p1],nums[p2]])
                print(currSum)

                if currSum == target:
                    res.append([fixed[0],fixed[1],nums[p1],nums[p2]])
                    p1+=1
                    while p1<p2 and nums[p1]==nums[p1-1]:
                        p1+=1
                elif currSum < target:
                    p1+=1
                else:
                    p2-=1

        recur(4,0,target)
        return res
        