class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        final =[]
        st=[]
        for i in range(len(temp)-1,-1,-1):

            while st and temp[i] >= st[-1][0]:
                    st.pop()
            if not st:
                final.append(0)
                st.append((temp[i],i))
            else:
                final.append(st[-1][1]-i)
                st.append((temp[i],i))
        
        return(final[::-1])
        