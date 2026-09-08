class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        for index in range(0, length):
            for j in range(index + 1, length):
                res[index] = res[index] * nums[j]
        index = length - 1
        while index >= 0:
            j = index - 1
            while j >= 0:
                res[index] = res[index] * nums[j]
                j -= 1
            index-=1

        print(res)
        return res