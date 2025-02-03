class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        res=[]
        st=[]
        def parent(opened,close):
            if opened == close == n:
                res.append(''.join(st))
            

            if opened <n:
                st.append('(')
                parent(opened+1,close)
                st.pop()
            
            if close <opened:
                st.append(')')
                parent(opened,close+1)
                st.pop()
        
        parent(0,0)
        return res