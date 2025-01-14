class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        Atrack = dict()
        cnt = 0
        res =[]
        for a in range(len(A)):
            Atrack[A[a]] = 1+Atrack.get(A[a],0)
            Atrack[B[a]] = 1+Atrack.get(B[a],0)
            print(Atrack)
            if Atrack[A[a]] >1:
                cnt+=1
            if A[a] != B[a] and Atrack[B[a]]>1:
                cnt+=1
           
            res.append(cnt)
        return res
            

        