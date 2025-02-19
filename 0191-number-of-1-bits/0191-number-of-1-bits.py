class Solution:
    def hammingWeight(self, n: int) -> int:

        return sum([1 for i in list(bin(n)) if i=='1'])
        