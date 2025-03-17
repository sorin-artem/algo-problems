class Solution:
    def divideArray(self, nums) -> bool:
        pairs = {}
        for num in nums:
            if num in pairs:
                pairs[num] += 1
            else:
                pairs[num] = 1
            if pairs[num] == 2:
                del pairs[num]


        return len(pairs.values()) == 0


print(Solution().divideArray([3,2,3,2,2,2,4]))