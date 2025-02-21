class Solution:
    def compress(self, chars: List[str]) -> int:
        
        indx =0   
        i=0     
        while i < len(chars):
            
            char = chars[i]
            cnt=0

            while i < len(chars) and char == chars[i]:
                cnt+=1
                i+=1
            
            chars[indx] = char
            indx+=1
            if cnt>1:
                st = str(cnt)
                for j in range(len(st)):
                    chars[indx]=st[j]
                    indx+=1
        return indx
        