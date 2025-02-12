class Solution:
    def titleToNumber(self, c: str) -> int:
        res=0

        for i in c:
            digit = ord(i) -ord('A')+1

            res = res*26 + digit
            print(res)
        return res

        