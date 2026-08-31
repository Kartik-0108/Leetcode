class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                current = nums[i] + nums[left] + nums[right]

                # Update closest
                if abs(current - target) < abs(closest - target):
                    closest = current

                # Exact match
                if current == target:
                    return current

                # Need a larger sum
                elif current < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return closest