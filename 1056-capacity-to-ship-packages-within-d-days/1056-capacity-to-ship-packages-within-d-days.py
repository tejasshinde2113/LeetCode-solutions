class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        arr=[max(weights), sum(weights)]

        def check(mid):
            cnt=1
            temp=0
            for i, a in enumerate(weights):
                if (mid ==6):
                    print("temp = " + str(temp)+ 'and cnt is ' + str(cnt))
                if temp+a<=mid:
                    temp+=a
                else:
                    temp=a
                    cnt+=1
            print(cnt)
            if cnt <= days :
                
                return True
            return False

        mid = None
        print(arr)
        res = sum(weights)
        while arr[0]<=arr[1]:
            mid = arr[0] + (arr[1]-arr[0])//2
            print(mid, arr)

            if check(mid):
               
                arr[1]= mid-1
                if mid ==6:
                    print('dh',arr)
                res = min(res,mid)
            else:
                arr[0]= mid+1
                
                
            
        return res
        