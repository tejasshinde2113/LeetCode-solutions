class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        final =[]
        st=[]
        for i in range(len(temp)-1,-1,-1):

            while st and st[-1][0] <= temp[i]:
                st.pop()
            if not st:
                st.append([temp[i],i])
                final.append(0)
            else:
                final.append(st[-1][1]- i )
                st.append([temp[i],i])
    
        return final[::-1]