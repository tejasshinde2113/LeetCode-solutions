class Solution:
    def isValid(self, s: str) -> bool:
        dct = {']':'[',')':'(','}':'{'}

        st=[]
        for i in s:
            st.append(i)
            while len(st)>1:
                if st[-2] == dct.get(st[-1],None):
                    st.pop()
                    st.pop()
                else:
                    break
            
        return not st