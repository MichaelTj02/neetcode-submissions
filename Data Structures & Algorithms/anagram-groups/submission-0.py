class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            grouped.setdefault(key, []).append(s)

        return list(grouped.values())
                