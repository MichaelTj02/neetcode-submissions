class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            curr = s[r]
            if curr not in count:
                count[curr] = 1
            else: count[curr] = count[curr] + 1

            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
            
            res = max(res, r - l + 1)

        return res