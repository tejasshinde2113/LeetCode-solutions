class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        st=[]
        final = 0
        for price in prices[::-1]:
            if st:
                if st[-1] > price:
                    final = max(final, st[-1]-price)
                else:
                    while st and st[-1] <= price:
                        st.pop()
                    if not st:
                        st.append(price)
                    else:
                        final = max(final, st[-1]-price)
                    
            else:
                st.append(price)
        return final
        