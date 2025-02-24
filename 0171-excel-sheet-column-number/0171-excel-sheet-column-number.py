class Solution:
    def titleToNumber(self, c: str) -> int:
        num =0
        print('A')
        for ch in c:
            cnt = ord(ch) - ord('A')+1

            num = num*26 + cnt
        
        return num

        