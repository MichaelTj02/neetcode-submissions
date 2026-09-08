class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for n in nums:
            numbers[n] = numbers.get(n, 0) + 1

        top_k = list(heapq.nlargest(k, numbers.keys(), key=numbers.get))

        return top_k