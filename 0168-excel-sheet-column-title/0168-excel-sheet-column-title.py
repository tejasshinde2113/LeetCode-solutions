class Solution:
    def convertToTitle(self, c: int) -> str:
        lst =[]
        while c > 0:
            c-=1
            lst.append(chr( ord('A') + c%26 ))
            c = c//26
        return ''.join(lst[::-1])