class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()

        left = 0
        right = len(tokens) - 1

        score = 0
        max_score = 0

        while left <= right:

            # Gain score using the cheapest token
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                max_score = max(max_score, score)
                left += 1

            # Gain power using the most expensive token
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1

            # Cannot make any move
            else:
                break

        return max_score