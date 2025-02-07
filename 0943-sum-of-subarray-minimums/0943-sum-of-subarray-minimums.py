class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        nsr = []
        st =[]
        i=len(arr)-1
        for n in (arr[::-1]):

            while st:
                if n > st[-1][0]:
                    nsr.append(st[-1][1]-i)
                    break
                else:
                    st.pop()
            if not st:
                nsr.append(len(arr) - i)
            st.append((n,i))
            i-=1
        

        nsr = nsr[::-1]


        nsl = []
        st =[]
        for i, n in enumerate(arr):

            while st:
                if n < st[-1][0]:
                    st.pop()
                    
                else:
                    nsl.append(i-st[-1][1])
                    break
                    
            if not st:
                nsl.append(abs(i -(-1)))
            st.append((n,i))

        
        res = [0]*len(arr)
        final =0

        for i,n in enumerate(arr):
            res[i] = n*nsl[i]*nsr[i]
            final = (final + n*nsl[i]*nsr[i])%(10**9 + 7)
        return final
        