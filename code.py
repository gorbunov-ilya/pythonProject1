from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int, k=None) -> int:
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k




