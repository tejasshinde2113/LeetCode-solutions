class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        print(lst)
        return (' '.join(lst[::-1]))
        