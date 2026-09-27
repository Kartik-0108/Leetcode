class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)

        left = 0
        right = n - 1

        # Find first position where order breaks from left
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        # Already sorted
        if left == n - 1:
            return 0

        # Find first position where order breaks from right
        while right > 0 and nums[right - 1] <= nums[right]:
            right -= 1

        # Find min and max inside the unsorted region
        minimum = min(nums[left:right + 1])
        maximum = max(nums[left:right + 1])

        # Expand left if needed
        while left > 0 and nums[left - 1] > minimum:
            left -= 1

        # Expand right if needed
        while right < n - 1 and nums[right + 1] < maximum:
            right += 1

        return right - left + 1