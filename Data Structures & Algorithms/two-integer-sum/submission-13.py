class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for index, elem in enumerate(nums):
            seen.setdefault(elem, index)
            diff = target - elem
            if diff in seen:
                res = [min(index, seen.get(diff)), max(index, seen.get(diff))]
                
        return res