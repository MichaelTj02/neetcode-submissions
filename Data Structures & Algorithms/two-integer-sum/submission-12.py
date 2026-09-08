class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            curr = nums[i]
            j = target - curr
            if j in numbers:
                jIndex = numbers.get(j)
                return [min(i, jIndex), max(i, jIndex)]

            if curr not in numbers:
                numbers[curr] = i
            
