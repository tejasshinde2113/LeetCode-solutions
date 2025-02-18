class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        

        p1=0
        n1=0
        res =[]
        while p1<len(pos) or n1 < len(neg):
            if p1 <len(pos) : res.append(pos[p1])
            if n1 < len(neg) : res.append(neg[n1])
            p1+=1
            n1+=1

        return res
