class Solution(object):
    def maxVowels(self, s, k):
        count = 0 # initializing the count variable to keep the track
        maxCount = 0
        vowel = ['a','e','i','o','u'] # a list of vowel to keep checking each element of the string s
        
        # Firstly taking the first window or we can say first subset 
        for i in range(0, k):
            if s[i] in vowel:
                count = count + 1
        maxCount = max(count , maxCount)
        
        # Now taking the remaining of the string and updating count accordingly 
        for i in range(k,len(s)):
            if s[i] in vowel:
                count = count + 1

            if s[i-k] in vowel:
                count = count - 1
            maxCount = max(count , maxCount)

        return maxCount
