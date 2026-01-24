from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        return max(
            self.helper(nums, firstLen, secondLen),
            self.helper(nums, secondLen, firstLen)
        )

    def helper(self, nums: List[int], L: int, M: int) -> int:
        n = len(nums)
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        maxL = 0
        result = 0

        for i in range(L + M, n + 1):
            maxL = max(maxL, prefix[i - M] - prefix[i - M - L])
            
            currentM = prefix[i] - prefix[i - M]
            result = max(result, maxL + currentM)

        return result
