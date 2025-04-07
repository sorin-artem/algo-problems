from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while True:
            res = numbers[l] + numbers[r]
            if res == target:
                return [l + 1, r + 1]
            if res > target:
                r -= 1
            else:
                l += 1


print(Solution().twoSum([100,200,300,500], 500))
