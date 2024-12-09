class Solution:
    def arrangeWords(self, text: str) -> str:

        lst = text.split()
        lst = sorted(lst,key = lambda x: len(x))

        for a in range(len(lst)):
            if a ==0:
                lst[a] = lst[a].title()
            else:
                lst[a] = lst[a].lower()
        return (" ").join(lst)
