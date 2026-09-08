class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        if len(s) == 2:
            if isAlphaNum(s[0]) and isAlphaNum(s[1]):
                if s[0].lower() != s[1].lower():
                    return False
            else:
                return True

        length = 0
        if len(s)/2 != 0:
            half = len(s)/2 - 1
        else:
            half = len(s)/2
        
        i = 0
        j = len(s) - 1
        while i < half:
            while not isAlphaNum(s[i]):
                i+=1
                if i > half:
                    return True
            while not isAlphaNum(s[j]):
                j-=1
                if j < half:
                    return True
            print(s[i], s[j])
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1

        return True

def isAlphaNum(c):
    return (ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9'))