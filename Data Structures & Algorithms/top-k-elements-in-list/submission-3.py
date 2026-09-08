class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        top_k = []

        for n in nums:
            if n in count:
                count[n] = count[n] + 1
            else:
                count[n] = 1
        
        sorted_dict = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))
        top_k = list(sorted_dict.keys())[:k]
        
        return top_k