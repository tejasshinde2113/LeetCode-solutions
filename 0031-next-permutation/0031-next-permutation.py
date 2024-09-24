class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        def reverseString(nums):
            for a in range(len(nums)//2):
                temp = nums[a]
                nums[a] = nums[len(nums)-1-a]
                nums[len(nums)-1-a] = temp

        def partial_in_place_sort(arr, start_index):
            for i in range(start_index + 1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= start_index and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
        
        f=-1
        for i in range(len(nums)-1,-1,-1):
            if(i>0):
                if(nums[i]>nums[i-1]):
                    f=i-1
                    break
        print(f)
        f2=0
        val = len(nums)-1
        if f==-1:
            reverseString(nums)
            nums = nums[::-1]
        else:
            for i,a in enumerate(nums):
                if i<f+1:
                    continue
                if(a>nums[f]):

                    if(f2==0):
                        val = i
                        f2=1
                    if(f2==1 and nums[i]<nums[val]):
                        val = i
     
            temp = nums[f]
    
            nums[f] = nums[val]
 
            nums[val] = temp
      
            partial_in_place_sort(nums, f+1)
     



        

        

        
        