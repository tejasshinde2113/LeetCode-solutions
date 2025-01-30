class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        st=[]
        temp = k
        for a in num:

            while st and k and int(st[-1])>int(a):
                st.pop()
                k-=1
            st.append(a)
        if k>0:
            st=st[:len(num)-temp]
       
        
        return ''.join(st).lstrip('0') or '0'

            