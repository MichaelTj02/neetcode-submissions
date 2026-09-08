class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for elem in nums:
            if elem in seen:
                return True
            seen[elem] = seen.setdefault(elem, 0) + 1
        return False