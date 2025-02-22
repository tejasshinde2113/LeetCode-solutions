class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res =[]

        q = deque([('(',1,0)])

        while q:

            output, opens, closes = q.popleft()

            if opens==closes==n:
                res.append(output)

            if opens < n:
                q.append((output +'(',opens+1,closes))
            if closes < opens:
                q.append((output + ')',opens,closes+1))
        return res        