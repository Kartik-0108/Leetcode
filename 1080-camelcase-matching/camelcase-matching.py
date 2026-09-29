class Solution:
    def camelMatch(self, queries, pattern):
        
        def matches(query):
            i = 0

            for char in query:

                # Character matches pattern
                if i < len(pattern) and char == pattern[i]:
                    i += 1

                # Unexpected uppercase character
                elif char.isupper():
                    return False

                # Otherwise char is lowercase, so ignore it

            return i == len(pattern)

        return [matches(query) for query in queries]