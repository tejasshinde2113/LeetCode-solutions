class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = deque([("", 0, 0)]) 
        
        while stack:
            s, opened, closed = stack.pop()
            
            if opened == closed == n:
                res.append(s)
                continue
            
            if opened < n:
                stack.append((s + "(", opened + 1, closed))
            
            if closed < opened:
                stack.append((s + ")", opened, closed + 1))
        
        return res


        # res=[]
        # st=[]
        # def parent(opened,close):
        #     if opened == close == n:
        #         res.append(''.join(st))
            

        #     if opened <n:
        #         st.append('(')
        #         parent(opened+1,close)
        #         st.pop()
            
        #     if close <opened:
        #         st.append(')')
        #         parent(opened,close+1)
        #         st.pop()
        
        # parent(0,0)
        # return res