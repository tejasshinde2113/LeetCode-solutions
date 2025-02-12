class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        

        for i in range(len(s)//2):

            if  len(s)%(i+1) ==0:
                cnt = len(s) / (i+1)

                st = s[:i+1]
                new=''
                for i in range(int(cnt)):
                    new =new+st
                if new == s:
                    return True
        
        return False