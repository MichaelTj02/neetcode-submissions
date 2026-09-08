class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS, charT = {}, {}

        for elem in s:
            charS[elem] = charS.setdefault(elem, 0) + 1
        for elem in t:
            charT[elem] = charT.setdefault(elem, 0) + 1

        if charS == charT:
            return True
        return False