class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            curr = w * h
            if curr > max: 
                max = curr

            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1

        return max