class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start =0
        N = len(letters)
        end = N-1
        res = None
        while start<=end:
            mid = start +(end-start)//2

            if(letters[mid]<=target):
                start= mid+1
            else:
                res = letters[mid]
                end = mid -1
        return res if res != None else letters[0]
        