class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        st = []

        for a in asteroids:
            st.append(a)
            while len(st)>1:
                if  (st[-1] < 0 and st[-2] >0):
                    if st[-1] == -st[-2]:
                        st.pop()
                        st.pop()
                        break
                    else:
                        
                        temp = None
                        if abs(st[-1]) > abs(st[-2]):
                            temp = st[-1]
                        else:
                            temp = st[-2]
                        st.pop()
                        st.pop()
                        st.append(temp)
                else:
                    break

                
        return st
        