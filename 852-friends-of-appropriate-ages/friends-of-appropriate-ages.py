class Solution:
    def numFriendRequests(self, ages):
        count = [0] * 121

        # Count how many people have each age
        for age in ages:
            count[age] += 1

        ans = 0

        for x in range(1, 121):
            if count[x] == 0:
                continue

            # y must satisfy:
            # y > 0.5*x + 7
            # y <= x

            for y in range(1, 121):
                if y <= 0.5 * x + 7:
                    continue

                if y > x:
                    continue

                # count[x] people can potentially request
                # count[y] people
                ans += count[x] * count[y]

                # A person cannot send a request to themselves
                if x == y:
                    ans -= count[x]

        return ans