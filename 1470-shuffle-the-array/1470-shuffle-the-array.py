class Solution(object):
    def shuffle(self, nums, n):
        output = []
        i = 0
        while i<n:
            output.append(nums[i])
            output.append(nums[i+n])
            i = i+1
        return output

        