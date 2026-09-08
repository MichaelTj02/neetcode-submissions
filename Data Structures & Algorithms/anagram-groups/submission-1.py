class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for s in strs:
            char = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                char[index] = char[index] + 1
            grouped.setdefault(tuple(char), []).append(s)

        return list(grouped.values())