class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        st=[]
        for ch in s:
            if st and st[-1][0] == ch:
                st[-1][1]+=1
            else:
                st.append([ch,1])
            
            if st and st[-1][1]==k:
                st.pop()


        res = ''
        for ch,cnt in st:
            res+=ch*cnt
        
        return res

        