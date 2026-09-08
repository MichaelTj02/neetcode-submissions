class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        table = {}
        longest = 0
        length = len(s)
        for right in range (0, length):
            current = s[right]
            if current not in table:
                table[current] = right
            else:
                left = max(left, table[current] + 1)
                table[current] = right

            longest = max(longest, right - left + 1)

        return longest    