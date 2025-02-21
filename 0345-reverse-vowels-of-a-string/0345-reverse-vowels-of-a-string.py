class Solution:
    def reverseVowels(self, s: str) -> str:

        vowel = set(['a','e','i','o','u','A','E','I','O','U'])
        s=list(s)
        p1=0
        p2=len(s)-1

        while p1<p2:

            if s[p1] not in vowel:
                p1+=1
                continue
            if s[p2] not in vowel:
                p2-=1
                continue
            
            s[p1],s[p2] = s[p2],s[p1]
            p1+=1
            p2-=1
        return ''.join(s)
        