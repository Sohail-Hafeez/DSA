class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        Max = -1
        for i in nums:
            if(i==1):
                count = count + 1
            else:
                Max = max(Max , count)
                count = 0
        return max(count , Max)

        