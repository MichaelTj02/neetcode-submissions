class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        substring = {}
        for s in s1:
            substring[s] = substring.get(s, 0) + 1

        l, window = 0, len(s1)
        while l + window <= len(s2):
            curr = {}
            i = l
            while i <= (l + window - 1):
                if s2[i]:
                    curr[s2[i]] = curr.get(s2[i], 0) + 1
                else:
                    return False
                i+=1
            print(curr)
            if curr == substring:
                return True
            else:
                l += 1

        return False