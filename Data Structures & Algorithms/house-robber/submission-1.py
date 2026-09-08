class Solution:
    def printCache(self, cache):
        for elem in cache:
            print(cache)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        for i in range(0, n):
            if i == 0:
                cache[i] = nums[i]
            elif i == 1:
                cache[i] = max(nums[0], nums[1])
            else:
                cache[i] = max(cache[i-1], nums[i] + cache[i-2])
        self.printCache(cache)
        return cache[n-1]