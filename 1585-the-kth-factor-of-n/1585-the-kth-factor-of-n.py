class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        cnt=0
        for i in range(1,n//2+1):
            if n%i == 0:
                cnt+=1
                if cnt==k:
                    return i
        return -1 if cnt+1 != k else n
        