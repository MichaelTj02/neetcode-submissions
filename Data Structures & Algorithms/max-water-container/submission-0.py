class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights)-1
        iHigh = False

        while i != j:
            if (heights[i] > heights[j]):
                height = heights[j]
                iHigh = True
            else:
                height = heights[i]
                iHigh = False

            width = j - i

            currArea = height*width
            print(currArea)
            if currArea>area:
                area = currArea
            
            if (iHigh):
                j-=1
                iHigh = False
            else:
                i+=1
                iHigh = False

        return area