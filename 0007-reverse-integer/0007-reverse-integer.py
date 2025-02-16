class Solution:
    def reverse(self, x: int) -> int:
        
        lmax = 2147483647
        lmin = 2147483648

        res =0

        neg = False
        if x <0:
            neg = True
            x = -x

        temp =x
        ans = 0
        while temp >0:
            digit = temp%10
            ans = ans*10 + digit

            if not neg and  ans/10 > lmax/10 or (ans == lmax/10 and  ans%10 > lmax%10):
                return 0
            if neg and  ans/10 > lmin/10 or (ans == lmin/10 and  ans%10 > lmin%10):
                return 0
            temp = temp//10
        return ans if not neg else -ans
