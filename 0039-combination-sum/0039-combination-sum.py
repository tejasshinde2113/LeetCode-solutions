class Solution:
    def combinationSum(self, ca: List[int], target: int) -> List[List[int]]:


        res =[]


        def check(total,ind,arr):

            if total == target:
                res.append(arr[:])
                return
            elif total > target:
                return 

            
            for i in range(ind,len(ca)):
                check(total+ca[i],i, arr+ [ca[i]])
        

        check(0,0,[])
        return res
        