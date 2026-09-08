class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pileLength = len(piles)
        res = max(piles)
        if pileLength == h:
            return res
        
        minK = 1
        maxK = res
        while minK <= maxK:
            mid = (minK+maxK)//2
            if mid == 0: mid = 1
            currRate = sum(math.ceil(p/mid) for p in piles)
            if currRate <= h:
                res = mid
                maxK = mid - 1
            else:
                minK = mid + 1

        return res