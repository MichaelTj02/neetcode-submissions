class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")

        import re
        s = re.sub(r'[^\w\s]', '', s)

        i = 0
        j = len(s) - 1

        while i <= (len(s)-1)/2:
            # print([s[i],s[j]])
            if s[i] != s[j]:
                return False
            i+=1
            j-=1

        return True
        