class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        st=[]
        final = 0
        for n in prices[::-1]:
            
            while st and   n > st[-1]:
                st.pop()
            if st and n <= st[-1]:
                final = max(final, st[-1]-n)
            else:
                st.append(n)

        return final

