class Solution:
    def countSegments(self, s: str) -> int:

        cnt =0
        res=0

        for a in s:
            if a == ' ':
                if cnt:
                    res+=1
                    cnt=0
            else:
                cnt+=1
        
        return res if not cnt else res+1
        