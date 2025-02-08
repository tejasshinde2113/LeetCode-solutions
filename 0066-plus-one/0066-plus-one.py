class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        cnt=1
        while i>=0:
            if digits[i]+cnt >9:
                digits[i] =0
                cnt =1
            else:
                digits[i]+=1
                cnt=0
                break
            i-=1

        if cnt :
            return [1]+digits
        
        return digits

        