from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        if window > len(s2):
            return False

        substring = Counter(s1)
        curr = Counter(s2[:window])  # first window

        if curr == substring:
            return True

        for i in range(window, len(s2)):
            # add the new character entering on the right
            curr[s2[i]] += 1

            # remove the character leaving on the left
            left_char = s2[i - window]
            curr[left_char] -= 1
            if curr[left_char] == 0:
                del curr[left_char]

            if curr == substring:
                return True

        return False