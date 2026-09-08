class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        nums.sort()
        for i in range(len(nums)):
            print(i)
            if i == len(nums) - 1:
                return False
            else:
                if nums[i] == nums[i+1]:
                    return True
        return False
        