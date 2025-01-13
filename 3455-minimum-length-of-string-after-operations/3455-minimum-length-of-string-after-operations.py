class Solution:
    def minimumLength(self, s: str) -> int:
        count = {}
        cnt=0
        for a in s:

            count[a] = 1+ count.get(a,0)
            if count[a]==3:
                count[a]-=2
            
        return sum(count.values())
        
        

        