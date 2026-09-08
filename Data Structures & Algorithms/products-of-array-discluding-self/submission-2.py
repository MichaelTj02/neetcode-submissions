class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        i = 1
        while i < len(nums):
            prefix[i] = prefix[i-1] * nums[i-1]
            i += 1
        j = len(nums) - 2
        while j > -1:
            suffix[j] = suffix[j+1] * nums [j+1]
            j -= 1

        res = [p * s for p, s in zip(prefix, suffix)]
        print(res)
        return res