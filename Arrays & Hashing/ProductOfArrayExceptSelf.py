from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            current_total = 1
            for j in range(len(nums)):
                if i == j:
                    continue

                current_total *= nums[j]

            output.append(current_total)

        return output

