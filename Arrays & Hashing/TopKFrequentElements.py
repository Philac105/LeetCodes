from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_dict = {}
        for num in nums:
            k_dict[num] = k_dict.get(num, 0) + 1

        most_frequents = []
        for i in range(k):
            most_frequent = max(k_dict, key=k_dict.get)
            k_dict.pop(most_frequent)
            most_frequents.append(most_frequent)

        return most_frequents