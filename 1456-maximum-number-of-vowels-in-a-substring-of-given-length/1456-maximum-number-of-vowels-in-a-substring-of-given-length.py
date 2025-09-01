class Solution(object):
    def maxVowels(self, s, k):
        vowels = set("aeiou")
        count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        maxCount = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:   # add new char
                count += 1
            if s[i-k] in vowels: # remove old char
                count -= 1
            maxCount = max(maxCount, count)

            # Early exit optimization: if we already found k vowels, can't get higher
            if maxCount == k:
                return k

        return maxCount
