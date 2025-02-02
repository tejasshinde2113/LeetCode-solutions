class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        st=[]
        res = []
        for price in prices[::-1]:
            if st:
                if st[-1] > price:
                    res.append(st[-1])
                else:
                    while st and st[-1] <= price:
                        st.pop()
                    if not st:
                        res.append(-1)
                        st.append(price)
                    else:
                        res.append(st[-1])
                        

            else:
                res.append(-1)
                st.append(price)
        res = res[::-1]

        final = 0
        for i,a in enumerate(prices):
            final = max(final,res[i]-a)
        return final
        