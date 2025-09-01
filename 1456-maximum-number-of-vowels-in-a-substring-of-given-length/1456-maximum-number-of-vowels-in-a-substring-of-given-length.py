class Solution(object):
    def maxVowels(self, s, k):
        count = 0
        maxCount = 0
        vowel = ['a','e','i','o','u']
        for i in s:
            if i in vowel and count < k:
                count = count + 1
                continue
            else:
                maxCount = max(count , maxCount)
                count = 0
        return max(count , maxCount)
