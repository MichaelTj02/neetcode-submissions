class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if diff not in seen:
                seen[nums[i]] = i
            else:
                if i < seen.get(diff):
                    return [i, seen.get(diff)]
                else:
                    return [seen.get(diff), i]
            i += 1



        