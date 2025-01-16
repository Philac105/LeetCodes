from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        most_consecutive = 0

        for i in range(len(nums)):
            current_consecutive = 1
            current_index = nums[i]

            j = 0
            while j < len(nums):
                if i == j:
                    j += 1
                    continue
                if nums[j] == current_index + 1:
                    j = 0
                    current_index += 1
                    current_consecutive += 1
                else:
                    j += 1

            if current_consecutive > most_consecutive:
                most_consecutive = current_consecutive

        return most_consecutive
