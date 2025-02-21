class Solution:
    def frequencySort(self, s: str) -> str:

        c= Counter(s)

        buck = [[] for i in range(len(s)+1)]

        for key,val in c.items():

            buck[val].append(key)


        res = []
        for i in range(len(buck)-1,-1,-1):
            if buck[i]:
                for ch in buck[i]:
                    res.append(ch*i)

        return ''.join(res) 
        