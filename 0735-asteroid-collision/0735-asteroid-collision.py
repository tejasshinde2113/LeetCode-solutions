class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        st= []
        p1=0
        p2=0

        while p2<len(asteroids):
            temp = asteroids[p2]
            f = True
            if not st :
                st.append(temp)
                p2+=1
                continue
            else:    
                while st:
                    
                    if(temp < 0 and st[-1] > 0) :
                        if abs(temp) > abs(st[-1]):
                            st.pop()
                        elif abs(temp) < abs(st[-1]):
                            f = False
                            break
                        else:
                            st.pop()
                            f = False
                            break
                    else:
                        break
            if f:
                st.append(temp)
            p2+=1

        return st
                        
        