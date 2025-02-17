class Solution:
    def simplifyPath(self, path: str) -> str:
        st= []
        dotcnt=0
        dot= False

        for a in path:

            while len(st) >1:
                if st[-1]==st[-2] and st[-1]=='/':
                    st.pop()
                else:
                    break

            if a=='.' and not dot:
                dot=True
                dotcnt = 0
            if a== '.':
                dotcnt+=1

            
            if a =='/' and dotcnt>0:
                if st[-1]!='.':
                    pass
                elif dotcnt ==1:
                    if st[-2]!='/':
                        pass
                    else:
                        st.pop()
                    
                elif dotcnt ==2:
                    if st[-3]!='/':
                        pass
                    else:
                        st.pop()
                        st.pop()
                        if st:
                            st.pop()
                        while st and st[-1] !='/':
                            st.pop()
                dotcnt=0
                dot=False
            st.append(a)

        if dotcnt>0:
            if st[-1]!='.':
                pass
            elif dotcnt ==1:
                if st[-2]!='/':
                    pass
                else:
                    st.pop()
                
            elif dotcnt ==2:
                if st[-3]!='/':
                    pass
                else:
                    st.pop()
                    st.pop()
                    if len(st)>1:
                        st.pop()
                    while len(st)>1 and st[-1] !='/':
                        st.pop()
                
        if len(st)==1:
            return st[0]
        
        while len(st)>1 and st[-1]=='/':
            st.pop()

        return ''.join(st)
        
            