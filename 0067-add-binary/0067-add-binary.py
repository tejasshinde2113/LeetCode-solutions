class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c=0
        n1 = len(a)-1
        n2= len(b)-1
        res =[]
        while n1>=0 or n2>=0:
            temp =0
            if n1>=0:
                temp += int(a[n1])
            if n2>=0:
                temp+=int(b[n2])
            temp += c
            if temp ==3:
                res.append('1')
                c=1
            elif temp == 2:
                res.append('0')
                c=1
            elif temp ==1:
                res.append('1')
                c=0
            else:
                res.append('0')
                c=0
            n1-=1
            n2-=1
        
        if c:
            res.append('1')

        return ''.join(res[::-1])