class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Max = 0
        d = 0

        for j in range(0, len(s)):
            a = []
            count = 0

            for i in range(d, len(s)):
                if s[i] not in a:
                    a.append(s[i])
                    count = count + 1
                else:
                    Max = max(count, Max)
                    break

            Max = max(Max, count)
            d = d + 1

        return Max