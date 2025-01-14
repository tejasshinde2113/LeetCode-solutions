class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        temp = k
        for a in num:

            while st and k and int(st[-1])>int(a):
                st.pop()
                k-=1
            st.append(a)
        st = st[:len(num)-temp]
        
        return ''.join(st).lstrip('0') or '0'

            
