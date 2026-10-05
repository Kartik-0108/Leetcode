class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0

        unique = set(nums)
class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0

        seen = set()
        pairs = set()

        for num in nums:
            if num - k in seen:
                pairs.add((num - k, num))

            if num + k in seen:
                pairs.add((num, num + k))

            seen.add(num)

        return len(pairs)
        if k == 0:
            return len(nums) - len(unique)  # ❌ not correct for unique pairs