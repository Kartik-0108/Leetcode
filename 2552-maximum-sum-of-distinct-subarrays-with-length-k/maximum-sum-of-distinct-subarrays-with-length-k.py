class Solution:
    def maximumSubarraySum(self, nums, k):
        left = 0
        current_sum = 0
        answer = 0
        window = set()

        for right in range(len(nums)):

            # Remove duplicates
            while nums[right] in window:
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # Add current element
            window.add(nums[right])
            current_sum += nums[right]

            # Keep window size at most k
            if right - left + 1 > k:
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # Valid window
            if right - left + 1 == k:
                answer = max(answer, current_sum)

        return answer