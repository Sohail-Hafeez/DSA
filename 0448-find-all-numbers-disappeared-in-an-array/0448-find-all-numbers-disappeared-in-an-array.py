class Solution(object):
    def findDisappearedNumbers(self, nums):
        output = []
        j = 1
        for i in range(len(nums)):
            if j in nums:
                j=j+1
                continue
            else:
                output.append(j)
                j=j+1
        return output


        