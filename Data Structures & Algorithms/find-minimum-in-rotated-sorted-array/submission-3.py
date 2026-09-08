class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        lowest = nums[0]

        while left <= right:
            mid = (left+right)//2
            if nums[mid] < lowest:
                lowest = nums[mid]
            
            if nums[left] <= nums[mid]:
                if nums[left] < lowest:
                    lowest = nums[left]
                if nums[mid] <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right = mid - 1
        return lowest
