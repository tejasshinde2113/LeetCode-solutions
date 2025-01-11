class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        elif len(s)==k:
            return True
        counter = {}
        for ch in s:
            counter[ch] = 1+ counter.get(ch,0)
        odd = len([num for num in counter.values() if num%2 != 0])

        return k-odd >=0
        