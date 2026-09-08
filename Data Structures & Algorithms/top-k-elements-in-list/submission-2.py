class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for elem in nums:
            table[elem] = table.setdefault(elem, 0) + 1
        res = []

        sorted_table = sorted(table, key=table.get, reverse=True)

        return sorted_table[:k]