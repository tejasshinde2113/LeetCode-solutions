class Solution:
    def reverse(self, x: int) -> int:
        
        lmax = 2147483647
        lmin = -2147483648

        res =0

        while x:
            temp = int(math.fmod(x,10))
            x = int(x/10)

            if res > int(lmax/10) or (res == int(lmax/10) and temp > int(lmax%10)):
                return 0
        
            if res < int(lmin/10) or (res == int(lmin/10) and temp < int(math.fmod(lmin,10))):
                return 0
            

            res = res*10+temp
        return res
