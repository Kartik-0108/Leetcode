class Solution:
    def expressiveWords(self, s, words):

        def is_stretchy(word):

            i = 0
            j = 0

            while i < len(s) and j < len(word):

                # Characters must match
                if s[i] != word[j]:
                    return False

                # Count group in s
                start_i = i
                while i < len(s) and s[i] == s[start_i]:
                    i += 1

                count_s = i - start_i

                # Count group in word
                start_j = j
                while j < len(word) and word[j] == word[start_j]:
                    j += 1

                count_word = j - start_j

                # Word cannot have more characters
                if count_word > count_s:
                    return False

                # If s has extra characters,
                # the group must have at least 3
                if count_s != count_word and count_s < 3:
                    return False

            # Both strings must be completely consumed
            return i == len(s) and j == len(word)

        count = 0

        for word in words:
            if is_stretchy(word):
                count += 1

        return count