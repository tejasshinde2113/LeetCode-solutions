class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        Atrack = set()
        cnt = 0
        res =[]
        for a in range(len(A)):
            if A[a] in Atrack:
                cnt+=1
            else:
                Atrack.add(A[a])
            if B[a] in Atrack:
                cnt+=1
            else:
                Atrack.add(B[a])
            
      
           
            res.append(cnt)
        return res
            

        