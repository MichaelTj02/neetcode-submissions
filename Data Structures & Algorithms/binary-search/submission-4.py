class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        return self.binarySearch(nums, target, left, right)

    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1
        mid = (right+left)//2
        print(mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid+1, right)
        else:
            return self.binarySearch(nums, target, left, mid-1)
        return -1

        