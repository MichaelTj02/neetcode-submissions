class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}

        for n in nums:
            if n not in numbers:
                numbers[n] = 1
            else:
                numbers[n] = numbers.get(n) + 1
        print(numbers)
        sorted_dict = dict(sorted(numbers.items(), key=lambda item: item[1], reverse=True))
        print(sorted_dict)
        sorted_number_list = list(sorted_dict.keys())

        return sorted_number_list[:k]
        